import ipaddress

network = '192.168.0.0/12'
ip = '192.168.0.1'

ip_add = ipaddress.ip_address(ip)
ip_net = ipaddress.ip_network(network, strict=False)
print(ip_add+2000)
print(ip_net)

for i in ip_net:
    print(i)