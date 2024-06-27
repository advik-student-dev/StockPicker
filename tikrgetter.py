import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

final_dict = {}

# URL to navigate
urls = ["https://stockanalysis.com/list/nasdaq-stocks/", "https://stockanalysis.com/list/nyse-stocks/", "https://stockanalysis.com/list/otc-stocks/", "https://stockanalysis.com/list/nyseamerican-stocks/"]


# Define a function to parse the current page and extract data
def parse_page(driver):
    global big_data_dict
    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table')

    # Extract headers
    headers = [header.text for header in table.find_all('th')]

    # Extract rows
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        row_data = [cell.text for cell in cells]
        rows.append(row_data)

    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers)

    return df


def main(url):
    # Initialize the webdriver
    driver = webdriver.Firefox()

    # Open the URL
    driver.get(url)

    # Extract data from the first page
    big_data = parse_page(driver)
    #print(big_data)

    # Keep clicking 'Next' and extracting data until the end
    while True:
        try:
            # Click the "Next" button
            driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/nav/button[2]').click()

            time.sleep(1)  # Wait for the page to load

            # Parse the new page
            new_data = parse_page(driver)

            # Append the new data to the existing data
            big_data = pd.concat([big_data, new_data], ignore_index=True)

        except Exception as e:
            print("No more pages to load or an error occurred:", e)
            break

    big_data_dict = big_data.set_index('Company Name ')['Symbol '].to_dict()
    print(big_data_dict)

    # Save the data to a file
    #with open("companies_and_tickers.txt", "w") as f:
        #f.write(str(big_data_dict) + "\n")

    # Close the driver
    driver.quit()
    #driver.close()
    return big_data_dict


for url in urls:
    print(url)
    new_data_dict = main(url)
    final_dict.update(new_data_dict)

print(final_dict)
with open("companies_and_tickers.txt", "w") as f:
    f.write(str(final_dict) + "\n")
