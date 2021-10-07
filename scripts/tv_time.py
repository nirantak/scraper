import os
from typing import Any

from dotenv import load_dotenv
from playwright.sync_api import Page, sync_playwright

load_dotenv()
TV_TIME: str = "https://www.tvtime.com"
USERID: str = os.environ.get("TV_TIME_USERID")
USERNAME: str = os.environ["TV_TIME_USERNAME"]
PASSWORD: str = os.environ["TV_TIME_PASSWORD"]
DEBUG: bool = True
OPTS: dict[str, Any] = {
    "ss_dir": "./screenshots",
    "headless": True,
    "slow_mo": 0,
}

if DEBUG:
    # Set DEBUG = True to see the browser in action
    os.environ["PWDEBUG"] = "console"
    # os.environ["PWDEBUG"] = "1"
    OPTS["headless"] = False
    OPTS["slow_mo"] = 100


def login(page: Page) -> None:
    page.goto(TV_TIME)
    page.click("text=Login")
    page.fill('[placeholder="Username/Email"]', USERNAME)
    page.fill('[placeholder="Password"]', PASSWORD)

    with page.expect_navigation():
        page.click('input:has-text("Login")')

    page.click(".optanon-alert-box-close")


def get_user_id(page: Page) -> str:
    page.goto(f"{TV_TIME}/en")
    page.click("text=Profile")
    res = page.url.split("/")[-2]
    print(f"User: {USERNAME} | ID: {res}")
    return res


def get_all_shows(page: Page) -> list[tuple[str, str]]:
    res = []
    page.goto(f"{TV_TIME}/en/user/{USERID}/profile")
    page.click("text=Shows")
    shows = page.query_selector_all("#all-shows .poster-details a")

    print(f"\nAll shows: {len(shows)}")
    for show in shows:
        show_name = show.inner_text().strip()
        show_url = f"{TV_TIME}{show.get_attribute('href')}"
        res.append((show_name, show_url))
        print(f"{show_name} [{show_url}]")

    return res


def get_stats_screenshot(page: Page) -> None:
    page.goto(f"{TV_TIME}/en/user/{USERID}/profile")
    page.click("text=Stats")
    page.screenshot(path=f"{OPTS['ss_dir']}/tv_time_stats.png", full_page=True)


if __name__ == "__main__":
    """
    For running in a repl, do:
        ```python
        from scripts.tv_time import *
        play = sync_playwright().start()
        ```
    followed by any commands you want to run.
    """

    with sync_playwright() as play:
        browser = play.chromium.launch(
            headless=OPTS["headless"], slow_mo=OPTS["slow_mo"]
        )
        page = browser.new_page()

        login(page)
        if not USERID:
            USERID = get_user_id(page)

        res = get_all_shows(page)
        get_stats_screenshot(page)

        browser.close()
