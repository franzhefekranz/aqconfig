from ping3 import ping

a= '192'
b= '168'
c= '1'
d= '1'

ip = a + '.' + b + '.' + c + '.' + d
print(ip)
if ping(ip) is None:
    txt = "Ping Test: " + "IP address does not reply" 
else:
        txt = "Ping Test" + "IP address is reachable"
print(txt)
    

