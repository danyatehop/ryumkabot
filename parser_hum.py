from bs4 import BeautifulSoup as bs
import fake_useragent
import requests


URL = "https://www.anekdot.ru/random/anekdot/"

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}


def hum_pars():

    html = requests.get(URL, headers=headers)

    soup = bs(html.text, 'html.parser')
    res = soup.find_all('div', class_='topicbox')

    humor = []

    for elem in res:
        humor.append(elem.find('div', class_='text'))

    res = str(humor[1]).replace("<br/>", "\n").replace("<br>", "\n")
    res = res.replace('<div class="text">', "").replace("</div>", "")

    return res
