import requests, json, math, pandas as pd
from bs4 import BeautifulSoup

# fake to become a browser
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

r = requests.get('https://www.openrice.com/en/hongkong/partialview/search',headers=headers)

soup = BeautifulSoup(r.text,"lxml")

print(soup)
