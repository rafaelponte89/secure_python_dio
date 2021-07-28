import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket created with success!!')
host = 'localhost'
port = 5483
message = 'Hi Server! How are you?'

try:
    print('Client: ' + message)
    s.sendto(message.encode(),(host,5482))
    data, server = s.recvfrom(4096)
    data = data.decode()
    print('Client: ' + data)
finally:
    print('Closing connection!')
    s.close()
