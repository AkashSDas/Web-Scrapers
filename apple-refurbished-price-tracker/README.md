# Apple Refurbished Price Tracker

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/AkashSDas)

[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/AkashSDas)

[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE)

## Table of contents

- 🧐 [ About](#about)

- 🔥 [Technologies Used](#technologies-used)

- 🛠 [Installation](#installation)

## About

> 🐍 Python script is used to scrape 🍎 Apple's website to get price of refurbished 💻 13.3-inch MacBook Pro.

> You can set the 💰 price at which you want to buy the MacBook and the run the script, once the price of that MacBook becomes `equal or less` to the price you had set, you will receive an 💌 `email` which will have the `URL and the current price of that MacBook.`

## Technologies Used

> [![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) is used as Programming Language.

> To send 🙏 request and get 🤲 response **`request`** package is used.

> To 🏋️‍♀️ parse the `HTML` received **`lxml`** and 🍜 **`Beautifulsoup4`** packages are used.

## Installation

> It is **recommended** to use **`virtual enviroment`** for this project to avoid any 😫 issues related to dependencies.

Here **`pipenv`** is used for this project.

- First, start by closing the repository

```bash
git clone https://github.com/AkashSDas/Web-Scrapers
```

- Go to the `apple-refurbished-price-tracker` folder

```bash
cd Web-Scrapers/apple-refurbished-price-tracker
```

- Install **`pipenv`** if you don't have it

```bash
pip install pipenv
```

- Once installed, access the venv folder inside the `apple-refurbished-price-tracker` folder

```bash
cd  venv/
```

- Create the virtual environment

```bash
pipenv install
```

The **Pipfile** of the project must be for creating replicating project's virtual environment.

This will install all the dependencies and create a **Pipfile.lock** (this should not be altered).

- Enable the virtual environment

```bash
pipenv shell
```

- The script file is in the `src` folder

```bash
cd src/
```

- Change `sender email address`, `sender email address password` and `receiver email address` to send and receive gmails.

```python
def  send_email(price):
	sender_email =  'sender@gmail.com'
	receiver_email =  'receiver@gmail.com'
	sender_email_password =  'password'

	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(send_email, sender_email_password)

		subject =  'Time To Buy'
		body =  f'The price of refurbished macbook pro 13-inch is now ${price}\n\n{URL}'
		msg =  f'Subject: {subject}\n\n{body}'

		smtp.sendmail(send_email, receiver_email, msg)
```

- To run the script do

```bash
python script.py
```
