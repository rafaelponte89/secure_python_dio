import socket
from colors import Colors as cl
cl = cl()
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(cl.colorIO('Socket Created','blue'))
host = 'localhost'
port = 10501

s.bind((host,port))
message = '\nServer: life!'
while 1:

    data, address = s.recvfrom(4096)
    if data:
        print(cl.colorIO('Received!','blue'))
        if data.decode() == '1':
            s.sendto(data + ('\nServer -> connected'.encode()),address)
        elif data.decode() == '2':
            s.sendto(data + ('\nServer -> impossible'.encode()),address)
        else:
            s.sendto(data + ('\nServer -> Closing'.encode()),address)
            s.close()




