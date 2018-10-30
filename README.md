# Scraper

> *A Python web scraper built using BS4 and Selenium*

### Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Requirements](#requirements)

### Installation

Clone the git repository:

```bash
$ git clone https://github.com/nirantak/scraper.git && cd scraper
```

Install necessary dependencies

```bash
$ pipenv install --dev
```

### Usage

Save Instagram username and password in the **.env** file as:

```shell
USERNAME="your_username_here"
PASSWORD="your_password_here"
```

Run script

```bash
$ pipenv run python instagram.py
```

### Requirements

1. [Python](https://python.org)
2. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
