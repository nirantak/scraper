#!/usr/bin/env python3

import os
from typing import Any

from playwright.sync_api import sync_playwright

DEBUG: bool = False
OPTS: dict[str, Any] = {
    "out_dir": "./out",
    "headless": True,
    "slow_mo": 0,
}

if DEBUG:
    # Set DEBUG = True to see the browser in action
    os.environ["PWDEBUG"] = "console"
    # os.environ["PWDEBUG"] = "1"
    OPTS["headless"] = False
    OPTS["slow_mo"] = 500

with sync_playwright() as play:
    browser = play.chromium.launch(
        headless=OPTS["headless"], slow_mo=OPTS["slow_mo"]
    )
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path=f"{OPTS['out_dir']}/user_agent.png")
    print(f"Title: \t\t{page.title()}")
    print(f"User Agent: \t{page.inner_text('.user-agent').strip()}")
    print(f"IP: \t\t{page.inner_text('.ip-address').split(':')[-1].strip()}")
    browser.close()
