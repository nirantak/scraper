# Scrapers

## Table of Contents

- [Scrapers](#scrapers)
  - [Table of Contents](#table-of-contents)
  - [Scripts](#scripts)
    - [TV Time](#tv-time)
    - [Archived](#archived)

## Scripts

### TV Time

- Environment variables or command line inputs: `TV_TIME_USERNAME`, `TV_TIME_PASSWORD`, `TV_TIME_USERID`
- Command line argument: `public` or `private`

  - If `public` is passed, the User ID is required (The username will be printed in the output).
  - If `private` is passed, a username and password will be needed to login (The user id will be printed in the output).

- To get the list of all your TV Shows, run the script:

  ```bash
  python scripts/tv_time.py [public|private]
  ```

- If no environment variables are set, the script will prompt for the same.
- Note: Currently Movies don't show up in the TV Time website, and the stats page is broken.

### Archived

Archived scrapers can be found [here](archive/).
