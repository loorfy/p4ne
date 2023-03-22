from pysnmp.hlapi import *

obj_ver = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.209", 161)),
                ContextData(),
                ObjectType(obj_ver)
                )

for received_data in result:
    for x in received_data[3]:
        print(x)

obj_ver_2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result_2 = nextCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.209", 161)),
                ContextData(),
                ObjectType(obj_ver_2),
                lexicographicMode=False
                )

for received_data in result_2:
    for x in received_data[3]:
        print(x)