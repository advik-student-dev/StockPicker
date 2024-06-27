from bs4 import BeautifulSoup
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pandas as pd
import numpy as np


def getprice(stock):
    url = "https://www.google.com/finance/quote/" + stock.upper() + ":NASDAQ?hl=en"
    HTML = requests.get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"},
    )
    soup = BeautifulSoup(HTML.text, "lxml")
    price: str = soup.find("div", attrs={"class": "YMlKec fxKbKc"}).text
    return price


def getStockMultiples_yFinance(stock):
    driver = webdriver.Firefox()

    with open("companies_and_tickers.txt", "r") as f:
        companies_tickers_dict = eval(f.read())

    #print(companies_tickers_dict)
    tikr = companies_tickers_dict[stock]
    all_yFinance_data = {'', ''}
    url = "https://finance.yahoo.com/quote/" + tikr
    #HTML = requests.get(
        #url,
        #headers={
            #"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"},
    #)
    driver.get(url)
    previous_close = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/div[2]/ul/li[1]/span[2]/fin-streamer').text
    open_price = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[2]/span[2]/fin-streamer').text
    bid = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[3]/span[2]').text
    ask = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[4]/span[2]').text
    days_range = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[5]/span[2]/fin-streamer').text
    volume = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[7]/span[2]/fin-streamer').text
    avg_volume = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[8]/span[2]/fin-streamer').text
    market_cap = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[9]/span[2]/fin-streamer').text
    beta = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[10]/span[2]').text
    pe_ratio = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[11]/span[2]/fin-streamer').text
    eps_ttm = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[12]/span[2]/fin-streamer').text
    target_est = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/section/section/article/div[2]/ul/li[16]/span[2]/fin-streamer').text

    data = [previous_close, open_price, bid, ask, days_range, volume, avg_volume, market_cap, beta, pe_ratio, eps_ttm, target_est]

    driver.quit()
    return data


if __name__ == "__main__":
    stock = input("Which stock: ")
    #price = getprice(stock)
    stock_data = getStockMultiples_yFinance(stock)
    print(stock_data)
    #print(price)
