import socket


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Socket server created!!')

host = 'localhost'
port = 5482

s.bind((host,port))
message = '\nServer: life!'

while 1:
    data, address = s.recvfrom(4096)
    if data:
        print('Server: sending!!')
        s.sendto(data + (message.encode()),address)