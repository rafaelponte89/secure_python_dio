import socket
import sys
from colors import Colors
color = Colors()

def main():
    try:
        # Creates socket (protocol IP, protocol TCP, comunication TCP
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        print(color.colorIO('The failed creation!!','red'))
        print(f'Error ===> {color.colorIO(e,"red")} <===')
        sys.exit()

    host_target = input(color.colorIO('Entry host or ip: ','blue'))
    port_target = input(color.colorIO('Entry port: ','blue'))
    try:
        s.connect((host_target,int(port_target)))
        print(color.colorIO('Success connection!!!','yellow'))
        s.shutdown(2)
    except socket.error as e:
        print(color.colorIO('The failed connection!!', 'red'))
        print(f'Error ===> {color.colorIO(e, "red")} <===')
        sys.exit()

if __name__ == '__main__':
    main()