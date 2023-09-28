from bs4 import BeautifulSoup as Bs
import fake_useragent
import requests


URL = "http://rzhunemogu.ru/Widzh/Tost.aspx"

user = fake_useragent.UserAgent().random

headers = {
    'user-agent': user
}


def toast_pars():

    html = requests.get(URL, headers=headers)

    soup = Bs(html.text, 'html.parser')
    res = soup.find('span', id='Label1')

    return res
