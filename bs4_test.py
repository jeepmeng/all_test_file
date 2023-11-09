# This is a sample Python script.
import bs4
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target = 'https://www.zhihu.com/question/295632125/answer/2596539804'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    texts = bs.find('div', id='content')
    print(type(texts))
    # print(texts.text.strip().split('\xa0' * 4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/