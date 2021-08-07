
# create word_list
def creation_list(_string,min=False,max=False,step=1):
    '''Generation word list'''
    import  itertools
    cont = 0

    # avoid the duplicity
    wd_set = set({})

    while min <= max:
        word_list_config = itertools.permutations(_string, min)  # tool to permutation
        for j in word_list_config:
            wd_set.add(''.join(j))  # add element in set
        min += step  # increase in 1
    return list(wd_set)

# word_list with configurations
def word_list(_string='', min=False, max=False, eq=False, numbers=False, \
              letters_lw=False, letters_up=False, opt=False, save=False):
    '''The configurations to generation word list'''


    # to available the digitation
    if opt:
        _string = input('Enter sequence: ')
        min= int(input('Length minimum: ' ))
        max = int(input('Length maximum: ' ))

    # option add numbers 0-9
    if numbers:
        for i in range (48,58):
            _string += ''.join(chr(i))

    # option add lowers characteres a-z
    if letters_lw:
        for i in range (97,123):
            _string += ''.join(chr(i))
            print(_string)

    # option add uppercase characteres A-Z
    if letters_up:
        for i in range (65,91):
            _string += ''.join(chr(i))

    wd_list = []
    if (min and max) > 0:
        wd_list = creation_list(_string,min=min,max=max)


    if eq: # permutation is executed about length of string
        wd_list = creation_list(_string,len(_string),len(_string))


    if save: # save list created in file
        import hashlib

        # hash based in string name, used md5 algorithm
        hash = hashlib.new('md5')
        hash.update(_string.encode('utf-8'))
        # summary hash

        name_file = 'word_list_' + str(hash.hexdigest()) + '.txt'
        length_ = len(wd_list)
        try:
            with open(name_file,'x') as file_:
                for i in wd_list:
                    file_.write(i + '\n')
        except FileExistsError as e:
            print('=' * 50)
            print('File already exist!!')
            print(f'{name_file}')
            print('='*50)

    return wd_list

# scan for word lists in current directory
def scan_word_lists():
   '''Find wordlists with prefix word_list in the type .txt'''

   import os
   word_lists=[]
   for i in os.listdir():
       if 'word_list' == i[0:9]:
           word_lists.append(i)

   return word_lists

def read_word_list(word_list):
    'Read word list saved in type .txt'
    if (word_list[0:9] == 'word_list') and (word_list[-4:] == '.txt'):
        with open(word_list,'r') as file_:
            content = file_.read()
            lines = content.splitlines()
        return lines
    else:
        print('Invalid word list to read!')


#print(word_list('morango',eq=True,save=True))
print(read_word_list(scan_word_lists()[0]))

