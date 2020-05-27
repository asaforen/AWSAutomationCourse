#!/usr/local/bin/python
import sys
import re

if sys.platform == 'win32':
    file = r'C:\WINDOWS\system32\drivers\etc\services'
else:
    file = 'services'

ports = set()
for line in open(file): 
   m = re.search(r'(\d+)/(udp|tcp)',line)
   if m:
       port = int(m.group(1))
       if port > 200: break
       ports.add(port)


print(set(range(1,201)) - ports)
