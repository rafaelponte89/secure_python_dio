import socket
import sys
from colors import Colors
color = Colors()

def scan():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        print('Failed creation socket!!!')
        print(f'Error: {e}')
        sys.exit()

    open = 'open'
    close = 'close'
    for i in range(0,65536):
        try:
            s.connect(('localhost',i))
            print(f'port {i} : {color.colorIO(open,"yellow")}')
            s.shutdown(1)
        except socket.error as e:
            pass
            #print(f'port {i} : {color.colorIO(close,"red")}')

scan()



