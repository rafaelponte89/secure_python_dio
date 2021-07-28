import requests
from bs4 import BeautifulSoup
from collections import Counter
import operator

def start_url(url):
    word_list = []
    req = requests.get(url).text
    soup = BeautifulSoup(req,'html.parser')

    for each_text in soup.find_all('div',class_='page'):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            word_list.append(each_word)
        clean_word(word_list)

def clean_word(word_list):
    clean_list = []

    for word in word_list:
        symbols = '(){}[]@#$%&*/-+.,?!|'
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],'')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if len(word)==5:
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key=operator.itemgetter(1)):
        print(' % s : % s ' % (key, value))
    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

start_url('https://www.moneytimes.com.br/')
