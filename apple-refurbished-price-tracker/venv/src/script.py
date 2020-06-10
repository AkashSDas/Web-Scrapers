# ****** Apple Refurbished Price Tracker ******


# *******************************

""" 
    *** Usage ***

    This script tracks price of mackbook pro 13-inch in Apple's
    refurbished website and sends a mail when the price is equal
    to or less than the price that you had set. 
"""

# *******************************

# ****** Importing Modules ******
import smtplib
import time

import lxml.html
import requests
from bs4 import BeautifulSoup

# ****** GLOBAL VARIABLES ******
BUY_AT_PRICE = 1099.00
URL = "https://www.apple.com/shop/product/FUHN2LL/A/refurbished-133-inch-macbook-pro-14ghz-quad-core-intel-core-i5-with-retina-display-space-gray?fnode=967ede1640460de801fd08be8545d04c003936c10908794cc2dcf3bec31bab2eb968a73b29285f05fcbcb750688d2990f4babb5fc9112ecf301d79a898a95032f9f903bdc9c775faca59b895ed2d18c5"


# ****** Sending request ******
def send_request(URL):
    response = requests.get(URL)
    try:
        source = response.text
        return source
    except:
        return f"Status Code: {response.status_code}"


# ****** Parsing the data ******
def parsing_data(source):
    soup = BeautifulSoup(source, 'lxml')

    price = soup.find_all("span", class_="current_price")
    price = float("".join(price[0].text.split()[0].split('$')[1].split(',')))

    return price


# ****** Send email ******
def send_email(price):
    sender_email = 'Sender email address'
    receiver_email = 'Receiver email address'
    sender_email_password = 'Password'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(send_email, sender_email_password)

        subject = 'Time To Buy'
        body = f'The price of refurbished macbook pro 13-inch is now ${price}\n\n{URL}'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(send_email, receiver_email, msg)


# ****** Comparing price ******
def buy_when_price_equal_to_my_price(URL, BUY_AT_PRICE):
    while True:
        source = send_request(URL)
        price = parsing_data(source)
        if price <= BUY_AT_PRICE:
            send_email(price)
            print('Email sent')


# ****** Calling the buy_when_price_equal_to_my_price function ******
buy_when_price_equal_to_my_price(URL, BUY_AT_PRICE)

# *******************************
