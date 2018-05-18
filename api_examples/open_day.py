from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://zik.ua/archive/all/2005/2/1?pg=1'
link = "https://zik.ua"


def get_all():
    links = []
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    soup = soup.find_all('li')
    i = 100
    article = link + soup[i].find('a').get('href')
    while not article.startswith('/rubric') and i < len(soup):
        try:
            links.append(article)
            article = link + soup[i].find('a').get('href')
        except AttributeError:
            continue
        finally:
            i += 1
    return links

