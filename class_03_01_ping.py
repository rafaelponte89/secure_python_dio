import os
from colors import Colors
color = Colors()
print('=' * 80)

# Calling the command ping through of module os
ip_host = input(color.colorIO('Set Ip or Host: ','blue'))
print(color.colorIO('-' * 80,'yellow'))
os.system('ping -c 3 {}'.format(ip_host))
print(color.colorIO('-' * 80,'yellow'))