import os
from colors import Colors
import time

color = Colors()
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    file.close()
    for ip in dump:
        print(color.colorIO('-'*50 ,'yellow'))
        os.system(f'ping -c 2 {ip}')
        print(color.colorIO('-' * 50, 'yellow'))
        time.sleep(5)