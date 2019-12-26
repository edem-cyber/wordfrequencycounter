import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup('a', class_=''):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)


def clean_up_list(wor_list):
    clean_word_list = []
    for word in word_list:
        symbols = "`~!@#$%^&*()_+{}|:\"<>?-=[];',./£\!"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')