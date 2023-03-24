from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, net=random.randint(0x0b000000, 0xdf000000), mask=random.randint(8, 24)):
        self.network = IPv4Network(net, strict=False)
        self.mask = mask
    def key_value(self):
        return int(self.network.network_address) + (self.mask)*2**32
    def network_address(self):
        return self.network_address
    def netmask(self):
        return self.mask


net_list = []
for i in (0, 50):
    net_list.append(IPv4RandomNetwork())
for n in sorted(net_list, key=n.key_value()):
    print(n)

