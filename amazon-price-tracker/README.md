# Amazon Price Tracker

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

> 🐍 Python script is used to scrape the 💵 price of a 📗 book in amazon among **top 10 sellers** and it gives the current lowest price's details.

> Url of that book's page on amazon 👉 [link](https://www.amazon.in/gp/offer-listing/0545289327/ref=dp_olp_all_mbc?ie=UTF8&condition=all)

#### Details of current lowest price book consists of:

- current time
- price of the book
- delivery method
- condition
- seller name
- seller ratings
- how many customers have rated the seller's services

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

- Go to the `amazon-price-tracker` folder

```bash
cd Web-Scrapers/amazon-price-tracker
```

- Install **`pipenv`** if you don't have it

```bash
pip install pipenv
```

- Once installed, access the venv folder inside the `amazon-price-tracker` folder

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
