import requests
from bs4 import BeautifulSoup
from newsplease import NewsPlease
from typing import List


#print(ap_topnews_list)

# techcrunch
techcrunch_url = 'https://techcrunch.com'
r_tech = requests.get(techcrunch_url)

soup_tech = BeautifulSoup(r_tech.content, 'html.parser')
atag_tech = soup_tech.find_all('a', attrs={"class": "post-block__title__link"})

tech_news_list = [i['href'] for i in atag_tech]
#print(tech_news_list)

# reuters news
reuters_news_url = 'https://www.reuters.com'
reuters_business_url = 'https://www.reuters.com/business/'
r_reuters = requests.get(reuters_business_url)

soup_reuters = BeautifulSoup(r_reuters.content, 'html.parser')
atag_reuters = soup_reuters.find_all('a', attrs={"data-testid": "Heading"})

reuters_business_list = [reuters_news_url + i['href'] for i in atag_reuters]
#print(reuters_business_list)

class ApNews:
    def __init__(self) -> None:
        pass

    def get_news(self, number_of_article=1) -> List[str]:
        # ap news
        # request
        ap_news_url = 'https://apnews.com'
        ap_topnews_url = 'https://apnews.com/hub/ap-top-news'
        r_ap = requests.get(ap_topnews_url)

        soup_ap = BeautifulSoup(r_ap.content, 'html.parser')
        atag_ap = soup_ap.find_all('a', attrs={"data-key": "card-headline"})
        ap_topnews_list = [ap_news_url + i['href'] for i in atag_ap]
        return ap_topnews_list[:number_of_article]
    
    def get_top_news(self) -> str:
        return self.get_news()[0]


ap = ApNews()
print(type(ap.get_news()))
print(ap.get_news())
print(ap.get_top_news())