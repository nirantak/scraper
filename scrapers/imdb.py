# Run: python -m scrapers.imdb

import os

from .utils import OPTS, Page, get_input, run_playwright

IMDB: str = "https://www.imdb.com/"
OPTS["email"] = os.environ.get("IMDB_EMAIL")
OPTS["password"] = os.environ.get("IMDB_PASSWORD")


def login(page: Page) -> None:
    # page.goto("/")
    # with page.expect_navigation():
    #     page.click('a[role="button"]:has-text("Sign In")')
    # page.click('a:has-text("Sign in with IMDb")')

    page.goto("/registration/ap-signin-handler/imdb_us")
    page.fill('input[name="email"]', OPTS["email"])
    page.fill('input[name="password"]', OPTS["password"])

    with page.expect_navigation():
        page.click('input[type="submit"]')


def get_user_id(page: Page, nav: bool = True) -> str:
    if nav:
        page.goto("/profile")
    OPTS["userid"] = page.url.split("/")[-2]
    return OPTS["userid"]


def get_user_name(page: Page, nav: bool = True) -> str:
    if nav:
        page.goto(f"/user/{OPTS['userid']}")
    OPTS["username"] = (
        page.query_selector(".user-profile h1").inner_text().strip()
    )
    return OPTS["username"]


def get_watchlist(page: Page, sort: str = "alpha,asc") -> None:
    """
    Possible sort methods: list_order, alpha, user_rating, moviemeter,
        your_rating, num_votes, release_date, runtime, date_added
    Possible sort orders: asc, desc
    Possible views: detail, grid
    """
    page.goto(f"/user/{OPTS['userid']}/watchlist?sort={sort}&view=detail")
    total = page.query_selector("div.lister-details").inner_text().strip()

    while page.is_visible(btn := "button.load-more"):
        page.click(btn)

    with page.expect_download() as download_info:
        page.click("div.export a")

    download_info.value.save_as(file := f"{OPTS['out_dir']}/imdb_watchlist.csv")
    print(f"\nDownloaded watchlist at: {file} with {total}")


def get_ratings(
    page: Page, sort: str = "your_rating,desc", rating: int = 0
) -> None:
    """
    Possible rating values: 1 to 10 (0 means all)
    Possible sort methods: your_rating, date_added
    Possible sort orders: asc, desc
    Possible modes: detail, grid
    """
    page.goto(
        f"/user/{OPTS['userid']}/ratings?sort={sort}&ratingFilter={rating}&mode=detail"
    )
    total = page.query_selector("div.lister-list-length").inner_text().strip()

    with page.expect_download() as download_info:
        page.click("div.vertical-ellipsis")
        page.click("a:has-text('Export')")

    download_info.value.save_as(file := f"{OPTS['out_dir']}/imdb_ratings.csv")
    print(f"\nDownloaded ratings at: {file} with {total}")


def get_stats_screenshot(page: Page) -> None:
    page.goto(f"/user/{OPTS['userid']}")
    page.click("#sidebar span.show-more")
    page.screenshot(path=f"{OPTS['out_dir']}/imdb_stats.png", full_page=True)


def main() -> None:
    with run_playwright(
        "chromium", base_url=IMDB, accept_downloads=True
    ) as page:
        page: Page
        page.goto("/")

        get_input(["email", "password"])
        login(page)
        get_user_id(page)
        get_user_name(page, False)
        print(f"\nUser: {OPTS['username']} | ID: {OPTS['userid']}")

        get_watchlist(page)
        get_ratings(page)
        get_stats_screenshot(page)


if __name__ == "__main__":
    """
    For running in a repl, do:
        ```python
        from scrapers.imdb import *
        play = sync_playwright().start()
        ```
    followed by any commands you want to run.
    """
    main()
