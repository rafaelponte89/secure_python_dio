import os

print('#'*20, ' MENU ', '#'*20)
print('1) Hidden File')
print('2) Show File')
op = int(input('Option: '))
name_file = input('Name file: ')




# hidden files in Linux
if op == 1:
    os.system('mv '+name_file+'.txt .file.txt')
elif op == 2:
# show file hidden  in Linux
    os.system('mv .'+ name_file+'.txt file.txt')
else:
    print('Option not exist!')