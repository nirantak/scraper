#!/usr/bin/env python3

import os
import pickle
from typing import Any, Dict, List, Set, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Config
CHROMEDRIVER_PATH: str = "./drivers/chromedriver_linux64"
COOKIES_PATH: str = "./cookies"
USERNAME: str = os.environ["IG_USERNAME"]
PASSWORD: str = os.environ["IG_PASSWORD"]


def login(driver: webdriver, username: str, password: str):
    # Load page
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for 2FA or Profile link to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
    )

    # Login
    driver.find_element_by_css_selector("input[name='username']").send_keys(username)
    driver.find_element_by_css_selector("input[name='password']").send_keys(password)
    driver.find_element_by_css_selector("button[type='submit']").click()

    # Wait for 2FA or Profile link to appear
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Profile"))
    )

    pickle.dump(
        driver.get_cookies(), open(f"{COOKIES_PATH}/instagram-cookies.pkl", "wb")
    )


def scrape_followers(
    driver: webdriver, username: str, cookies: List[Dict[str, Any]] = None
) -> Tuple[str, str, Set[str], Set[str]]:
    # CSS Selector for followers and following lists
    list_css: str = "div[role='dialog'] a.notranslate"

    if cookies:
        # Load any page before setting cookies
        driver.get("https://www.instagram.com/data/manifest.json")
        for cookie in cookies:
            driver.add_cookie(cookie)

    # Load account page
    driver.get(f"https://www.instagram.com/{username}/")

    num_followers: str = driver.find_element_by_css_selector(
        "a[href*='followers'] span"
    ).text
    num_following: str = driver.find_element_by_css_selector(
        "a[href*='following'] span"
    ).text

    # Click the 'Followers' link
    driver.find_element_by_partial_link_text("followers").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, list_css))
    )
    # TODO: Scrolling Magic here
    _followers: List = driver.find_elements_by_css_selector(list_css)
    followers: Set[str] = {i.text for i in _followers}

    driver.find_element_by_css_selector(
        "div[role='dialog'] button span[aria-label='Close']"
    ).click()

    # Click the 'Following' link
    driver.find_element_by_partial_link_text("following").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, list_css))
    )
    # TODO: Scrolling Magic here
    _following: List = driver.find_elements_by_css_selector(list_css)
    following: Set[str] = {i.text for i in _following}

    return (num_followers, num_following, followers, following)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("window-size=1200x700")

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

    try:
        try:
            cookies: List[Dict[str, Any]] = pickle.load(
                open(f"{COOKIES_PATH}/instagram-cookies.pkl", "rb")
            )
        except FileNotFoundError:
            login(driver, USERNAME, PASSWORD)

        num_followers, num_following, followers, following = scrape_followers(
            driver, USERNAME, cookies
        )

        print(f"{USERNAME}: {num_followers} followers, {num_following} following")
        print(f"\nFollowers: {followers}")
        print(f"\nFollowing: {following}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
