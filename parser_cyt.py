from bs4 import BeautifulSoup as bs
import fake_useragent
from random import randint
import requests


URL = "https://citatko.com/bez-rubriki/auf-tsitaty-pro-volkov"

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}


def cyt_pars():
    html = requests.get(URL, headers=headers)

    soup = bs(html.text, 'html.parser')
    res = soup.find_all('div', class_='ads-color-box')
    index = randint(0, len(res))

    return res[index].text
