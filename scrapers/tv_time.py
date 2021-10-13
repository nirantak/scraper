# Run: python -m scrapers.tv_time [public|private]

import os
import sys

from .utils import OPTS, Page, get_input, run_playwright

TV_TIME: str = "https://www.tvtime.com"
OPTS["userid"] = os.environ.get("TV_TIME_USERID")
OPTS["username"] = os.environ.get("TV_TIME_USERNAME")
OPTS["password"] = os.environ.get("TV_TIME_PASSWORD")


def login(page: Page) -> None:
    page.goto("/")
    page.click("text=Login")
    page.fill('[placeholder="Username/Email"]', OPTS["username"])
    page.fill('[placeholder="Password"]', OPTS["password"])

    with page.expect_navigation():
        page.click('input:has-text("Login")')


def get_user_id(page: Page) -> str:
    page.goto("/en")
    page.click("text=Profile")
    OPTS["userid"] = page.url.split("/")[-2]
    return OPTS["userid"]


def get_user_name(page: Page) -> str:
    page.goto(f"/en/user/{OPTS['userid']}/profile")
    OPTS["username"] = (
        page.query_selector(".profile-infos h1.name").inner_text().strip()
    )
    return OPTS["username"]


def get_all_shows(page: Page) -> list[tuple[str, str]]:
    res = []
    page.goto(f"/en/user/{OPTS['userid']}/profile")
    page.click("text=Shows")
    shows = page.query_selector_all("#all-shows .poster-details a")

    print("\nList of Shows:\n")
    for show in shows:
        show_name = show.inner_text().strip()
        show_url = f"{TV_TIME}{show.get_attribute('href')}"
        res.append((show_name, show_url))
        print(f"{show_name} [{show_url}]")

    print(f"\nUser: {OPTS['username']} | ID: {OPTS['userid']}")
    print(f"Total Shows: {len(shows)}")
    return res


def get_stats_screenshot(page: Page) -> None:
    page.goto(f"/en/user/{OPTS['userid']}/profile")
    page.click("text=Stats")
    page.screenshot(path=f"{OPTS['out_dir']}/tv_time_stats.png", full_page=True)


if __name__ == "__main__":
    """
    For running in a repl, do:
        ```python
        from scrapers.tv_time import *
        play = sync_playwright().start()
        ```
    followed by any commands you want to run.
    """
    mode = sys.argv[1] if len(sys.argv) > 1 else "private"

    with run_playwright("chromium", base_url=TV_TIME) as page:
        page: Page
        page.goto("/")
        page.click(".optanon-alert-box-close")

        if mode == "private":
            get_input(["username", "password"])
            login(page)
            if OPTS["userid"] is None:
                get_user_id(page)
        elif mode == "public":
            get_input(["userid"])
            if OPTS["username"] is None:
                get_user_name(page)
        else:
            print("\nInvalid mode.\n")
            sys.exit(1)

        get_all_shows(page)
        get_stats_screenshot(page)
