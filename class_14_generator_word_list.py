
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
            cont += step            # count number of words
        min += step  # increase in 1
    return list(wd_set), cont

# word_list with configurations
def word_list(_string='', min=False, max=False, eq=False, numbers=False, \
              letters_lw=False, letters_up=False, opt=False, save=False):
    '''The configurations to generation word list'''
    name_file = None
    cont = 0
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
    if (min and max > 0):
        wd_list = creation_list(_string,min=min,max=max)
        cont = wd_list[1]

    if eq: # permutation is executed about length of string
        wd_list = creation_list(_string,len(_string),len(_string))
        cont = wd_list[1]

    if save: # save list created in file
        import hashlib

        # hash based in string name, used md5 algorithm
        hash = hashlib.new('md5')
        hash.update(_string.encode('utf-8'))
        # summary hash
        name_file = 'word_list_' + str(hash.hexdigest()) + '.txt'

        try:
            with open(name_file,'x') as file:
                for i in wd_list[0]:
                    file.write(i + '\n')
        except FileExistsError as e:
            print('File aready exist!!')




    return wd_list, name_file, cont

# scan for word lists in current directory
def scan_word_lists():
   import os
   word_lists=[]
   for i in os.listdir():
       if 'word_list' == i[0:9]:
           word_lists.append(i)
   return word_lists



word_list('morango',eq=True)
