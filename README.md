# Scrape-My-Car
A BeautifulSoup web scraper to help you find your dream car, designed for scalability in mind. You can easily create new sources and tags, passing them directly into the existing function. The scraper is set to scrape once every 24 hours, and send an email if it gets a match.


## Setup

Ensure python 3.9 is installed.

Install requirements:
```bash
pip install -r requirements.txt
```

Or, create a virtual environment:
```bash
pip install pipenv
pipenv shell
pipenv update
```

## Instructions

You must set up a .env file for the environment variables used, including the proxy email, password, mail server, etc. The scraper will continue to use this info unelss told otherwise.

## Running the Scraper

```
python scrape.py
```
