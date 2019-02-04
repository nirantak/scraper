#!/usr/bin/env python3

import locale
from datetime import datetime
from typing import Set, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Config
URL: str = "full_url_here"
SCREENSHOT_PATH: str = "./screenshots"
CHROMEDRIVER_PATH: str = "./drivers/chromedriver_linux64"
locale.setlocale(locale.LC_ALL, "en_US.UTF8")


def get_price(driver: webdriver) -> Tuple[datetime, str, Set[str]]:
    driver.get(URL)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Book")  # Button like 'Book' or 'Confirm'
        )
    )

    # CSS selectors for currency and price elements on page
    currency = driver.find_elements_by_css_selector("p.price_info span")
    prices = driver.find_elements_by_css_selector("p.price_info span.num")

    timestamp = datetime.now()

    driver.get_screenshot_as_file(
        f"{SCREENSHOT_PATH}/ticket-prices_{timestamp.strftime('%d-%m-%Y_%H-%M-%S')}.png"
    )

    return timestamp, currency[0].text, {locale.atof(i.text) for i in prices}


def write_price():
    pass


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1280x720")

    with webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options) as driver:
        try:
            timestamp, currency, prices = get_price(driver)
            print(
                f"{timestamp.strftime('%d-%m-%Y %H:%M:%S')} -- {currency} {min(prices)}"
            )
        except Exception as e:
            print(f"Error: {e}")
