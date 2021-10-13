# Scraper

> _Python web scrapers built using Selenium, BS4 and Playwright_

## Table of Contents

- [Scraper](#scraper)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Requirements](#requirements)

## Installation

Clone the git repository:

```bash
git clone https://github.com/nirantak/scraper.git && cd scraper
cp -nv .env.sample .env  # copy and update the env variables
```

Install necessary dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel setuptools
pip install -U -r requirements.txt
playwright install
```

## Usage

See [scrapers/README.md](scrapers/) for usage instructions.

Samples present in [demo/](demo/).

## Requirements

1. [Python 3.10](https://www.python.org/downloads/)
