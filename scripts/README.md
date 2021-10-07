# Scrapers

## Table of Contents

- [Scrapers](#scrapers)
  - [Table of Contents](#table-of-contents)
  - [Scripts](#scripts)
    - [TV Time](#tv-time)
    - [Archived](#archived)

## Scripts

### TV Time

Required environment variables: `TV_TIME_USERNAME`, `TV_TIME_PASSWORD`

Optional environment variables: `TV_TIME_USERID`

To get the list of all your TV Shows, run the script after setting the required environment variables:

```bash
python scripts/tv_time.py
```

If `TV_TIME_USERID` is not set, the script will find and output the User ID.

Note: Currently Movies don't show up in the TV Time website, and the stats page is broken.

### Archived

Archived scrapers can be found [here](archive/).
