from news_extractor import ApNews, TechCrunch, Reuters
from news_summarizer import OpenAIGPT
from newsplease import NewsPlease

ap = ApNews()
tech = TechCrunch()
reuters = Reuters()

ap_top_article = NewsPlease.from_url( ap.get_top_news_url())
tech_top_article = NewsPlease.from_url(tech.get_top_news_url())
reuters_top_article = NewsPlease.from_url(reuters.get_top_news_url())

gpt_summarizer = OpenAIGPT()

print(ap_top_article.title)
print("\n")
print(ap_top_article.maintext)
print(gpt_summarizer.summarize(ap_top_article.maintext))
print("\n\n")

# print(tech_top_article.title)
# print("\n")
# print(tech_top_article.maintext)
# print(gpt_summarizer.summarize(tech_top_article.maintext))
# print("\n\n\n")

# print(reuters_top_article.title)
# print("\n")
# print(reuters_top_article.maintext)
# print(gpt_summarizer.summarize(reuters_top_article.maintext))
# print("\n\n\n")