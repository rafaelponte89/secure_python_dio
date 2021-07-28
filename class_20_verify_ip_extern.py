import json
from urllib.request import urlopen
import socket
import ipaddress
from colors import Colors

color = Colors()

host = input('Enter with site or ip: ')
url = 'none'
ip_host='none'
try:
    # try convert in typ ip
    ip_host = ipaddress.ip_address(host)

except:

    # catch ip by name
    ip_host = socket.gethostbyname(host)

finally:
    # create the link with ip
    url = 'https://ipinfo.io/'+str(ip_host)+'/json'

if ip_host != 'none':
    response = urlopen(url)
    dice = json.load(response)
    try:
        print(color.colorIO('IP: ','blue'), color.colorIO(dice['ip'],'yellow'))
        print(color.colorIO('Host Name: ','blue'), color.colorIO(dice['hostname'],'yellow'))
        print(color.colorIO('City: ','blue'), color.colorIO(dice['city'],'yellow'))
        print(color.colorIO('Region: ','blue'), color.colorIO(dice['region'],'yellow'))
        print(color.colorIO('Country: ','blue'), color.colorIO(dice['country'],'yellow'))
    except KeyError as e:
        print(e)