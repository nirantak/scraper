# Scraper
> *A Python web scraper built using BS4 and Selenium*

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Requirements](#requirements)

### Installation
Clone the git repository:
```Shell
$ git clone https://github.com/nirantak/scraper.git && cd scraper
```

Install necessary dependencies
```Shell
$ pip install -r requirements.txt
```

### Usage
Save Instagram username and password in file **config.json** as:
```JSON
{
    "username":"your_username_here",
    "password":"your_password_here"
}
```
Run script
```Shell
$ python instagram.py
```

### Requirements
1. [Python](https://python.org)
2. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

