from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                              random.randint(p_start, p_end)),
                             strict=False
                             )

    def regular(self):
        return self.is_global and not \
            (self.is_multicast or self.is_link_local or \
             self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)

    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)

def sortfunc(x):
    return x.key_value()

net_list = []
for i in (0, 50):
    net_list.append(IPv4RandomNetwork(8, 24))
for n in sorted(net_list, key=sortfunc):
    print(n)

