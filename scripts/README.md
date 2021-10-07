# Scrapers

## Table of Contents

- [Scrapers](#scrapers)
  - [Table of Contents](#table-of-contents)
  - [Scripts](#scripts)
    - [TV Time](#tv-time)
    - [Archived](#archived)

## Scripts

### TV Time

- Environment variables: `TV_TIME_USERNAME`, `TV_TIME_PASSWORD`, `TV_TIME_USERID`
- If `TV_TIME_PASSWORD` is set, it will be used along with `TV_TIME_USERNAME` to log in to TV Time.
  - `TV_TIME_USERID` is optional in this case, and if not set the script will find and output the User ID.
- If `TV_TIME_PASSWORD` is not set then `TV_TIME_USERID` is required, and the script will assume it is a public profile and continue without login.
  - `TV_TIME_USERNAME` is optional in this case, and if not set the script will find and output the username.
- To get the list of all your TV Shows, run the script after setting the required environment variables:

  ```bash
  python scripts/tv_time.py
  ```

- Note: Currently Movies don't show up in the TV Time website, and the stats page is broken.

### Archived

Archived scrapers can be found [here](archive/).
