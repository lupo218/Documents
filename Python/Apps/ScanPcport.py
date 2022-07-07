from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos import Device

host = 'x.x.x.x'
dev = Device(host, user='root', password='xxx')
ss = StartShell(dev)
commnad = f"cli -c 'show ethernet-switching table detail| no-more'"
ss.open()
cmd_1_result = (ss.run(commnad))[1]
ss.close()

cmd_1_result

sting1 = cmd_1_result.replace(',', '') # split to line
sting1 = sting1.splitlines()

for i in sting1:
    if i.find('VLAN:'):
        print(i)


