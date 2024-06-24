from bs4 import BeautifulSoup
import requests

def getArticles(stock, exchange):
    url = "https://www.google.com/finance/quote/" + stock.upper(
    ) + ":" + exchange.upper()+"?hl=en"
    HTML = requests.get(
        url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"})
    soup = BeautifulSoup(HTML.text, "lxml")
    listOfLinks = []
    for i in soup.select("a.TxRU9d"):
        listOfLinks.append(i['href'])

    with open("links.txt", "a") as file:
        print(stock.upper() + "\n", file=file)
        print(*listOfLinks, sep="\n", file=file)
        print("\n", file=file)
    return listOfLinks


if __name__ == "__main__":
    stock = input("Which stock: ")
    exchange = input("Which exchange: ")
    link = getArticles(stock, exchange)
    print(link)
