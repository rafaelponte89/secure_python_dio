
def word_list(string,min,max):
    import itertools
    while min <= max:
        word_list_config = itertools.permutations(string, min)
        for j in word_list_config:
            print(''.join(j))
        min +=1

string = input('Enter sequence: ')
min= int(input('Length minimum: ' ))
max = int(input('Length maximum: ' ))
word_list(string,min,max)

