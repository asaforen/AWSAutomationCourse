import re

#service_list = open('/etc/services','r')
'''
with open(r'/etc/services','r') as file:
    for line in file:
        m = re.search(r'(\d+)/(udp|tcp)',line)
        port_list = set()
        if m:
            port = int(m.groups()[0])
            #print(port)
            if port > 200:
                break
            
            port_list.add(m)
            print(set(range(1-200)) - port_list)
'''
file = r'/etc/services'

ports = set()
for line in open(file): 
   m = re.search(r'(\d+)/(udp|tcp)',line)
   if m:
       port = int(m.group(1))
       if port > 200: break
       ports.add(port)


print(ports)