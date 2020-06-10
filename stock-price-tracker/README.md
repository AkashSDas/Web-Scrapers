# Stock Price Tracker

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

> 🐍 Python script is used to scrape the 💸 **stock details** of a given company from **Yahoo's Finance website**.

> This stock details are save to **`csv file`** of name as `CompanyStockName.csv`.

> An example of a company's stock summary on Yahoo's Finance website 👉 [Tesal Stock's](<[https://finance.yahoo.com/quote/TSLA?p=TSLA](https://finance.yahoo.com/quote/TSLA?p=TSLA)>)

#### This stock detail consists of

- Time
- Previous Close
- Open,Bid
- Ask
- Day's Range
- 52 Week Range
- Volume
- Avg. Volume
- Market Cap
- Beta (5Y Monthly)
- PE Ratio (TTM)
- EPS (TTM)
- Earnings Date
- Forward Dividend & Yield
- Ex-Dividend Date
- 1y Target Est

## Technologies Used

> [![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) is used as Programming Language.

> To send 🙏 request and get 🤲 response **`request`** package is used.

> To 🏋️‍♀️ parse the `HTML` received **`lxml`** and 🍜 **`Beautifulsoup4`** packages are used.

> 🐼 `Pandas` package is used to work with data and add them to csv file.

## Installation

> It is **recommended** to use **`virtual environment`** for this project to avoid any 😫 issues related to dependencies.

Here **`pipenv`** is used for this project.

- First, start by closing the repository

```bash
git clone https://github.com/AkashSDas/Web-Scrapers
```

- Go to the `stock-price-tracker` folder

```bash
cd Web-Scrapers/stock-price-tracker
```

- Install **`pipenv`** if you don't have it

```bash
pip install pipenv
```

- Once installed, access the venv folder inside the `stock-price-tracker` folder

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

- To run the script do

```bash
python script.py
```
