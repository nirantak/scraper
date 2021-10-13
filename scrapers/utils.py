import os
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from playwright.sync_api import (
    Browser,
    BrowserType,
    Page,
    Playwright,
    sync_playwright,
)

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEBUG: bool = os.environ.get("DEBUG", "false").lower() == "true"
OPTS: dict[str, Any] = {
    "out_dir": PROJECT_ROOT / "out",
    "headless": True,
    "slow_mo": 0,
}

if DEBUG:
    # Set DEBUG = True to see the browser in action
    os.environ["PWDEBUG"] = "console"
    # os.environ["PWDEBUG"] = "1"
    OPTS["headless"] = False
    OPTS["slow_mo"] = 200


def get_input(fields: list[str]) -> list[str]:
    res = []
    for field in fields:
        OPTS[field] = (OPTS[field] or input(f"Enter {field.upper()}: ")).strip()
        res.append(OPTS[field])
    return res


@contextmanager
def run_playwright(browser_type: str, base_url: str | None = None) -> Page:
    """
    browser: 'chromium', 'webkit' or 'firefox'
    """
    play: Playwright = sync_playwright().start()
    browser: BrowserType = getattr(play, browser_type)
    window: Browser = browser.launch(
        headless=OPTS["headless"], slow_mo=OPTS["slow_mo"]
    )
    page: Page = window.new_page(base_url=base_url)

    try:
        yield page
    finally:
        window.close()
        play.stop()
