# This rpm does a lot of the setup but python3.6 is required
# and there is some trickery involved along with flask needing
# to be installed via pip3

Name:		vm-audit	
Version:	0.0.2
Release:	2%{?dist}
Summary:	A python web service that creates yaml file for vm or machine info

Group:		Applications/Internet
License:	MIT
URL:		https://github.com/jmiahman/vm-audit
Source0:	https://github.com/jmiahman/%{name}/archive/%{version}.tar.gz

BuildRequires:	centos-release-scl-rh rh-python36-python-setuptools rh-python36
Requires:	centos-release-scl-rh rh-python36 rh-python36-PyYAML supervisord
 
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
python3 setup.py install --root=$RPM_BUILD_ROOT --install-lib=%{python_sitearch}

rm -rf $RPM_BUILD_ROOT/usr/lib64/python2.7

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
%attr(-, vmaudit, vmaudit)%config /etc/%{name}/%{name}.cfg
%attr(-, vmaudit, vmaudit)%config /etc/supervisord.d/%{name}.ini
%attr(-, vmaudit, vmaudit)%dir %{_localstatedir}/cache/%{name}
%attr(-, vmaudit, vmaudit)%dir %{_localstatedir}/log/%{name}

%changelog
* Thu Nov 29 2018 JMiahMan <jmiahman@unity-linux.org> - 0.0.2-2
- Add supervisord support and some notes

* Thu Nov 29 2018 JMiahMan <jmiahman@unity-linux.org> - 0.0.2-1
- Some changes

* Thu Nov 29 2018 JMiahMan <jmiahman@unity-linux.org> - 0.0.1-1
- Initial build
