from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos import Device
import sys


def get_vlan(interfaces,host): #get the vlan name on the interfaces
    dev=Device(host, user='root', password='xxx')
    ss = StartShell(dev)
    commnad = f"cli -c 'show ethernet-switching interfaces {interfaces} | no-more'"
    ss.open()

    cmd_1_result = (ss.run(commnad))[1]
    cmd_1_result = (cmd_1_result).split("Blocking")[1]
    cmd_1_result = (cmd_1_result).split(" ")[8]
    cvlan = cmd_1_result
    ss.close()
    return cvlan



def Set_vlan(interfaces,host,nvlan): # Set the New Vlan
    Old_Vlan = get_vlan(interfaces,host)
    print(Old_Vlan)
    dev=Device(host, user='root', password='xxx')
    ss = StartShell(dev)
    commnad = f"cli -c 'edit | no-more;edit interfaces {interfaces}| no-more;replace pattern {Old_Vlan} with  {nvlan} | no-more;commit | no-more'"
    commnad2 = f"cli -c 'edit | no-more;edit interfaces {interfaces}| no-more;set disable | no-more;commit | no-more'"
    commnad3 = f"cli -c 'edit | no-more;edit interfaces {interfaces}| no-more;delete disable | no-more;commit | no-more'"
    ss.open()
    ss.run(commnad)
    ss.run(commnad2)
    ss.run(commnad3)
    print(get_vlan(interfaces,host))
    ss.close()




print(Set_vlan('ge-0/0/27','x.x.x.241','ptusers-f4'))

