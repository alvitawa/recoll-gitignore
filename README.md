
Find all .gitignored root directories and files and add them to recoll's `skippedPaths` setting. This will exclude all .gitignored files from recoll indexing.

## Setup

`pip install -r requirements.txt`

Add line `skippedPaths = ` to `.recoll/recoll.conf` if it is not already there.

## Run on home directory:

`./crawler.py ~`

The script will override whatever your `skippedPaths` configuration was.