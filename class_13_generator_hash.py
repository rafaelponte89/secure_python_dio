import hashlib
import sys

string = input('Text to code: ')
menu = {'MD5':1,'SHA1':2,'SHA256':3,'SHA512':4}

print('#'*20,'MENU GENERATOR HASH', 20 * '#')
for key, values in menu.items():
    print(values,')', key)
string = string.encode()
option = int(input('Choice algorithm hash: '))
hash = list(menu.keys())
menu = list(menu.values())

if menu[0] == option:
    overcome = hashlib.md5(string)
    hash = hash[0]
elif menu[1] == option:
    overcome = hashlib.sha1(string)
    hash = hash[1]
elif menu[2] == option:
    overcome = hashlib.sha256(string)
    hash = hash[2]
elif menu[3] == option:
    overcome = hashlib.sha512(string)
    hash = hash[3]
else:
    print('Something given wrong!')
    sys.exit()
file = open('hashes.txt','a')
text = file.write(overcome.hexdigest() + ' : ' + hash + '\n')
file.close()
