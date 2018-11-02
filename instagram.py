#!/usr/bin/env python3

import os
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver: webdriver, username: str, password: str):
    # Load page
    driver.get("https://www.instagram.com/accounts/login/")

    # Login
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    # Wait for 2FA or Profile link to appear
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Profile"))
    )


def scrape_followers(driver: webdriver, username: str) -> List[str]:
    # Load account page
    driver.get(f"https://www.instagram.com/{username}/")

    # Click the 'Followers' link
    driver.find_element_by_partial_link_text("follower").click()

    # Wait for the followers modal to load
    xpath = "//div[@style='position: relative; z-index: 1;']/div/div[2]/div/div[1]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # TODO: Scrolling Magic Here #

    # Scrape the followers
    xpath = "//div[@style='position: relative; z-index: 1;']//ul/li/div/div/div/div/a"
    followers_elems = driver.find_elements_by_xpath(xpath)

    return [e.text for e in followers_elems]


if __name__ == "__main__":
    driver = webdriver.Chrome("drivers/chromedriver_linux64")
    user = os.environ["IG_USERNAME"]
    passwd = os.environ["IG_PASSWORD"]

    try:
        login(driver, user, passwd)
        followers = scrape_followers(driver, user)
        print(followers)
    finally:
        driver.quit()
