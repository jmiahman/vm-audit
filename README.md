# vm-audit
This is just a super simple example I use for a RHCSA II class for messing with curl and webapi stuff, it's not really meant to be used for anything meaningful except as an example application that has a web api.

This is a small script that does a few things. It listens for 5 things.
- A Hostname: the name of the local machine.
- The user: The use that is running the http post
- The Core or CPU count: How many processor(s) cores are on the machine
- The overall or Total Physical Memory Amount
- The physical drive size for the first or main disk drive

Once these are passed to this web service it creates a file for each host
that contains that hosts information

To create a yaml file with system information:

curl http://hostname-or-ip:5000/audit/hostname/user/cpu/memory/hdsize
