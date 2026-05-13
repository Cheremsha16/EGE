from ipaddress import ip_address, ip_network

ip_1 = ip_address('200.154.190.12')
ip_2 = ip_address('200.154.184.0')

for mask in range(0, 14):
    net_1 = ip_network(f'{ip_1}/{mask}', False)
    net_2 = ip_network(f'{ip_2}/{mask}', False)
    if ip_1 in net_1.hosts() and \
            ip_2 in net_2.hosts():
        print(net_1.netmask)