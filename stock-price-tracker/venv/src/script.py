# ****** Stock Price Tracker ******


"""
    - In this project Yahoo Finance webiste is scraped.

    - Using this scraper we can get stock details of companies
      whose stocks are present in Yahoo's Finance webiste.

    - This scraper returns stock detail of an individual company
      after a certain period of time, by default this time period
      is 1 hour.

    - If you want to customize the time period then you can provide
      the amount of time(in seconds) after which you want to get stock
      details of the specified company.

    - The stock details of the company are added to a csv file which is
      named CompanyStockName.csv(this file is automatically created)
      after the specified time period.
"""


# ****** Importing Modules ******
import datetime
import os.path
import time

import lxml.html
import pandas as pd
import requests
from bs4 import BeautifulSoup


# ****** Sending the request ******
def send_request(company):
    URL = f'https://finance.yahoo.com/quote/{company}?p={company}'
    response = requests.get(URL)
    try:
        source = response.text
        return source
    except:
        return f'Status Code: {response.status_code}'


# ****** Parsing the data ******
def parsing_data(source):
    soup = BeautifulSoup(source, 'lxml')

    fields = soup.find_all('td', class_="C($primaryColor) W(51%)")
    fields = [field.text for field in fields]

    values = soup.find_all('td', class_="Ta(end) Fw(600) Lh(14px)")
    values = [value.text for value in values]

    summary = {}
    summary['Time'] = datetime.datetime.now().strftime('%d %B %Y %I:%M:%S')
    for field, value in zip(fields, values):
        summary[field] = [value]

    return summary


# ****** Save the data received csv file ******

# The name of the csv file is => company.csv
# where 'company' is the stock name of that company
# in Yahoo's Finance website.

def add_to_csv(company, summary):
    if os.path.isfile(f'{company}.csv'):
        df = pd.DataFrame(summary)
        df.to_csv(f'{company}.csv', mode='a', index=False, header=False)
    else:
        with open(f'{company}.csv', 'w') as file:
            df = pd.DataFrame(summary)
            df.to_csv(f'{company}.csv', index=False)


# ****** Getting the stock details after a specific period  ******
# time_period: after how long you want to add stock details
#              to the csv file.
# it's default value if 60*60 i.e. 1 hour

def get_stock_data(company, time_period=60*60):
    while True:
        source = send_request(company)
        summary = parsing_data(source)
        add_to_csv(company, summary)

        time.sleep(time_period)


# ****** Calling the get_stock_data function ******

# Company name of whose stock summary we want
company = 'TSLA'

# Getting stock details after every 1 second
get_stock_data(company, time_period=1)

# But this might take more than 1 second since it
# has to request to the server for that page html.
