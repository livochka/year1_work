from mercury_parser.client import MercuryParser
from html.parser import HTMLParser
from open_day import get_all

parser = MercuryParser(api_key='545DJojPyFRExaJ85WlGym4K7T9s3RiK2ZAd7DVi')
article = parser.parse_article('https://zik.ua/news/2005/02/01/u_natsionalnomu_muzei_vidkryto_vystavku_z_nagody_75richchya_z_dnya_narodzhennya_45')
p = article.json()['content']


class MyHTMLParser(HTMLParser):
    info = []

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        pass

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        print(data)


parser2 = MyHTMLParser()
parser2.feed(p)
