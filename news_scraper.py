from GoogleNews import GoogleNews
import pandas as pd



googlenews = GoogleNews(lang='en', period='1d')
googlenews.get_news('something')