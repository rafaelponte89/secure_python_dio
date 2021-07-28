# create word_list
def creation_list(word_list_config):
    '''Generation word list'''
    wd_list = []
    for j in word_list_config:
        #print(''.join(j))
        wd_list.append(''.join(j))
    return wd_list

# word_list with configurations
def word_list(_string='', min=False, max=False, eq=False, numbers=False, \
              letters_lw=False, letters_up=False, opt=False):
    '''The configurations to generation word list'''
    import itertools

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
    if  (min and max) > 0:
        while min <= max:
            word_list_config = itertools.permutations(_string, min) # tool to permutation
            wd_list = creation_list(word_list_config) # call creation_list
            min +=1 # increase in 1

    if eq: # permutation is executed about length of string
        word_list_config = itertools.permutations(_string)
        wd_list = creation_list(word_list_config)

    return wd_list

print(word_list(opt=True))
#
# # table ascii
# # 48-57 numbers
# # 32-47  e 58 - 64 e  91-96 e 123-126 special caracteres
# # 97 - 122 lower
# # 65 - 90 upper
# numbers = input('Enter numbers:')
#
# if numbers == '1':
#     for i in range (48,57):
#         string += ''.join(chr(i))
# elif numbers == '2':
#     for i in range (65,91):
#         string += ''.join(chr(i))
#
#
# print(word_list(string,min,max))

