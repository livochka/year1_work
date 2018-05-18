from mercury_parser.client import MercuryParser
from html.parser import HTMLParser
from open_day import get_all

parser = MercuryParser(api_key='545DJojPyFRExaJ85WlGym4K7T9s3RiK2ZAd7DVi')
links = get_all()[0:10]

info = []

class MyHTMLParser(HTMLParser):
    info = []

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        pass

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        global info
        print(data)
        info.append(data)

parser2 = MyHTMLParser()

for i in links:
    try:
        article = parser.parse_article(i)
        p = article.json()['content']
        parser2.feed(p)
        print('+', i)
    except AttributeError:
        continue

print(info)

