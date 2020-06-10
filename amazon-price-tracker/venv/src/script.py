# ****** Amazon Price Tracker ******


"""
    *** Usage ***

    This script tracks price of a book among top 10 sellers and 
    gives the current lowest price among them.
"""


# ****** Importing Modules ******
import datetime
import time

import lxml.html
import requests
from bs4 import BeautifulSoup

# ****** GLOBAL VARIABLE ******
URL = "https://www.amazon.in/gp/offer-listing/0545289327/ref=dp_olp_all_mbc?ie=UTF8&condition=all"


# ****** Sending request ******
def send_request(URL):
    try:
        response = requests.get(URL)
        source = response.text
        return source
    except:
        return f"Status Code: {response.status_code}"


# ****** Parsing the data ******
def parsing_data(source):
    soup = BeautifulSoup(source, 'lxml')

    seller_names = soup.find_all('span', class_="a-size-medium a-text-bold")
    seller_names = [" ".join(seller_name.text.split())
                    for seller_name in seller_names]

    prices = soup.find_all('div', class_="olpPriceColumn")
    prices = [float(price.text.split()[1]) for price in prices]

    product_conditions = soup.find_all(
        'span', class_="a-size-medium olpCondition a-text-bold")
    product_conditions = [product_condition.text.split()[0]
                          for product_condition in product_conditions]

    product_shipping_data = soup.find_all('p', class_="olpShippingInfo")
    product_shipping = []
    for product in product_shipping_data:
        product = product.text.split()
        if product[0] == '+':
            product_shipping.append(f'{product[0]}{product[1]} {product[2]}')
        elif len(product) == 2:
            product_shipping.append(f'{product[0]} {product[1]}')
        elif len(product) == 9:
            product_shipping.append(
                f'{product[0]} {product[1]} {product[2]} {product[3]} {product[4]} {product[5]}{product[6]}')

    seller_ratings = []
    seller_positive_percentage = []
    total_ratings = []
    seller_and_product_details = soup.find_all('p', class_="a-spacing-small")
    for details in seller_and_product_details:
        details = details.text.split()
        seller_ratings.append(details[0])
        seller_positive_percentage.append(details[5])
        total_ratings.append(details[-3].split('(')[1])

    parsed_data = zip(prices, product_shipping, product_conditions, seller_names,
                      seller_ratings, seller_positive_percentage, total_ratings)
    parsed_data = list(parsed_data)

    return parsed_data


# ****** Getting lowest price ******
def get_lowest_price_product_data(URL):
    source = send_request(URL)
    parsed_data = parsing_data(source)

    if len(parsed_data) > 0:
        lowest_price_product_data = parsed_data[0]
        for data in parsed_data:
            if data[0] < lowest_price_product_data[0]:
                lowest_price_product_data = data

        lowest_price_product_data = list(lowest_price_product_data)
        today_datetime = datetime.datetime.now().strftime('%d %B %Y %I:%M:%S')
        lowest_price_product_data.insert(0, today_datetime)

        return lowest_price_product_data
    else:
        return 'Try Again'


# ****** Calling the get_lowest_price_product_data function ******
print(get_lowest_price_product_data(URL))
