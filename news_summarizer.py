from news_extractor import ApNews, TechCrunch, Reuters
from newsplease import NewsPlease
import openai
import os
from dotenv import load_dotenv

load_dotenv("./.env")
openai.api_key = os.getenv('OPENAI_KEY')

class OpenAIGPT:
    def __init__(self) -> None:
        pass
    
    def summarize(self, prompt: str):
        augmented_prompt = f"summarize this text: {prompt}"
        summarized_text = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
        return summarized_text


# ap = ApNews()
# tech = TechCrunch()
# reuters = Reuters()

# ap_top_article = NewsPlease.from_url( ap.get_top_news_url())
# tech_top_article = NewsPlease.from_url(tech.get_top_news_url())
# reuters_top_article = NewsPlease.from_url(reuters.get_top_news_url())

# print(tech_top_article.title)
# print(tech_top_article.maintext)

# print(type(tech_top_article.maintext))

# gpt_summarizer = OpenAIGPT()
# print(gpt_summarizer.summarize(tech_top_article.maintext))