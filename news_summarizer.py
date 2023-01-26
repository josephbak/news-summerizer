from news_extractor import ApNews, TechCrunch, Reuters
from newsplease import NewsPlease

ap = ApNews()
ap_top_url = ap.get_top_news_url()

# tech = TechCrunch()
# print(tech.get_top_news_url())

# reuters = Reuters()
# print(reuters.get_top_news_url())

print(NewsPlease.from_url(ap_top_url).title)
print(NewsPlease.from_url(ap_top_url).maintext)