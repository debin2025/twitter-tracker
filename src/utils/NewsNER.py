from GoogleNews import GoogleNews
from TweetNER import news_ner_gen
from collections import Counter

def news_ner():
    news = GoogleNews(lang='en', region='US', period='1d')
    news.search('Politics')
    news.get_page(2)
    news.get_page(3)
    news.get_page(4)
    count = Counter()
    result_count = 0
    for result in news.results():
        result_count+=1
        ner_list = news_ner_gen(result["title"])
        for ner in ner_list:
            count[ner]+=1
    return count

def news_ner_rank(rank):
    return news_ner().most_common(3)[rank][0]
