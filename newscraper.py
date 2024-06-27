import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def get_news():
    base_url = 'https://www.cnbc.com/2024/06/21/apple-ai-europe-dma-macos.html'
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
    elif "yahoo" in base_url:
        driver = webdriver.Firefox()
        driver.get(base_url)
        try:
            driver.find_element(By.XPATH, '//*[@id="caas-art-e54c21cf-6997-3e27-b5ad-ccecc871b5e6"]/article/div/div/div/div/div/div/div[2]/div[2]/div[2]/button').click()
        except Exception as e:
            print("Article likely does not have a 'Story Continues' button in Yahoo \nLink " + base_url)
            print(e)
        try:
            elems = driver.find_element(By.XPATH, '//*[@id="caas-art-e54c21cf-6997-3e27-b5ad-ccecc871b5e6"]/article/div/div/div/div/div/div/div[2]/div[2]').text
        except Exception as e:
            print(e)

        driver.quit()

    elif "bloomberg" in base_url:
        driver = webdriver.Firefox()
        driver.get(base_url)
        try:
            elem = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/article[1]/div[5]/div/div[2]/div[3]').text
            print(elem)
        except Exception as e:
            print(e)
        driver.quit()

    elif "bbc" in base_url:
        driver = webdriver.Firefox()
        driver.get(base_url)
        try:
            elem = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/div[3]').text
            print(elem)
        except Exception as e:
            print(e)
        driver.quit()

    else:
        print("Can't read this. My bad")


get_news()
