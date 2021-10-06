# Scraper

> _Python web scrapers built using Selenium, BS4 and Playwright_

## Table of Contents

- [Scraper](#scraper)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Ticket Price Scraper](#ticket-price-scraper)
    - [Instagram Followers Scraper](#instagram-followers-scraper)
  - [Requirements](#requirements)

## Installation

Clone the git repository:

```bash
git clone https://github.com/nirantak/scraper.git && cd scraper
```

Install necessary dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel setuptools
pip install -U -r requirements.txt
```

## Usage

### Ticket Price Scraper

Fill all variables in the top **# Config** section.

Run script

```bash
python scripts/ticket_prices.py
```

### Instagram Followers Scraper

Rename file **sample.env** as **.env**, and fill all environment variables (username, password).

Run script

```bash
python scripts/instagram.py
```

## Requirements

1. [Python 3.10](https://www.python.org/downloads/)
2. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
