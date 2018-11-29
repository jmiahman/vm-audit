Name:		vm-audit	
Version:	0.0.1
Release:	1%{?dist}
Summary:	A python web service that creates yaml file for vm or machine info

Group:		Applications/Internet
License:	MIT
URL:		https://github.com/jmiahman/vm-audit
Source0:	https://github.com/jmiahman/%{name}/archive/%{version}.tar.gz

BuildRequires:	python36-setup-tools python36
Requires:	python36
 
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
This is a small script that does a few things. It listens for 5 things.

A Hostname: the name of the local machine.
- The user: The use that is running the http post
- The Core or CPU count: How many processor(s) cores are on the machine
- The overall or Total Physical Memory Amount
- The physical drive size for the first or main disk drive
Once these are passed to this web service it creates a file for each host that contains that hosts information

%prep
%setup -q

%build

%install
python3 setup.py install

%pre
/usr/bin/getent group vmaudit > /dev/null || /usr/sbin/groupadd -r vmaudit
/usr/bin/getent passwd vmaudit > /dev/null || /usr/sbin/useradd -r -d /path/to/program -s /sbin/nologin -g vmaudit vmaudit

%postun
if [ "$1" == 0 ]; then
   userdel --force vmaudit 2> /dev/null; true
fi

%files
%doc README.md
%{_bindir}/%{name}
%attr(-, vmaudit, vmaudit) %{_configdir}/%{name}.cfg
%attr(-, vmaudit, vmaudit)%{_localstatedir}/cache/%{name}
%attr(-, vmaudit, vmaudit)%{_localstatedir}/log/%{name}

%changelog
* Thu Nov 29 2018 JMiahMan <jmiahman@unity-linux.org> - 0.0.1-1
- Initial build
