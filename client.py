import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = 'localhost'
port = '10500'

while 1:
    data_client = input('Data Client: ')
    s.sendto(data_client.encode(),(host,10501))
    data,server = s.recvfrom(4096)
    data = data.decode()
    print('\nMessage Client' + data)
    if 'Closing' in data:
        print('Closing connection client')
        s.close()
        break