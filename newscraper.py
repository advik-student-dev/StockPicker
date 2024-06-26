import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_news():
    base_url = 'https://finance.yahoo.com/news/1-unstoppable-stock-could-join-070000643.html'
    html_text = requests.get(base_url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    # CNBC Article Parser
    if "cnbc" in base_url:
        article_headline = soup.find(class_='ArticleHeader-headline').text

        full_article_text = ""
        article_text_list = soup.find_all(class_="group")
        for article_text in article_text_list:
            full_article_text += article_text.text
        print(article_headline)
        print(full_article_text)


    # Yahoo Article Parser
    if "yahoo" in base_url:
        blind = soup.find(class_="caas-body")
        for blinds in blind:
            print(blinds.text)




get_news()