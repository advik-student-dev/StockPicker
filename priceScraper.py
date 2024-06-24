from bs4 import BeautifulSoup
import requests



def getprice(stock, exchange):
    url = "https://www.google.com/finance/quote/"+ stock.upper() + ":" + exchange.upper() + "?hl=en"
    HTML = requests.get(
        url,
        headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"},
        )
    soup = BeautifulSoup(HTML.text, "lxml")
    price = soup.find("div",attrs={"class":"YMlKec fxKbKc"}).text
    return price


if __name__ == "__main__":
    stock = input("Which stock: ")
    exchange = input("Which exchange: ")
    price = getprice(stock, exchange)
    print(price)
