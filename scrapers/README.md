# Scrapers

## Table of Contents

- [Scrapers](#scrapers)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [TV Time](#tv-time)
    - [IMDb](#imdb)
    - [Archived](#archived)

## Usage

- Environment variables:
  - `DEBUG`: `true` to enable debug mode and show browser interactions.

### TV Time

- Environment variables or command line inputs: `TV_TIME_USERNAME`, `TV_TIME_PASSWORD`, `TV_TIME_USERID`
- Command line argument: `public` or `private`

  - If `public` is passed, the User ID is required (The username will be printed in the output).
  - If `private` is passed, a username and password will be needed to login (The user id will be printed in the output).

- To get the list of all your TV Shows, run the script:

  ```bash
  python -m scrapers.tv_time [public|private]
  ```

- If no environment variables are set, the script will prompt for the same.
- Note: Currently Movies don't show up in the TV Time website, and the stats page is broken.

### IMDb

- Environment variables or command line inputs: `IMDB_EMAIL`, `IMDB_PASSWORD` to login.
- To download your Watchlist and Ratings data, run:

  ```bash
  python -m scrapers.imdb
  ```

- If no environment variables are set, the script will prompt for the same.

### Archived

Archived scrapers can be found [here](archive/).
