a = """
import os
os.system('pip install lxml bs4')
os.system('pip install pytelegrambotapi')
"""
exec(a)


from lxml import html
from bs4 import BeautifulSoup
import requests

url = 'https://github.com/mixgx/SocialParse/blob/main/test.md'
r = requests.get(url)
htmlf = r.content.decode()

soup = BeautifulSoup(htmlf, features="lxml")
test = soup.find('article', {'class': 'markdown-body entry-content container-lg'}).text

if test == 'lol\n':
    print('ds')