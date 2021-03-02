#!/usr/bin/python3

import os
from tqdm import tqdm
import argparse

from gitignore_parser import parse_gitignore

parser = argparse.ArgumentParser()
parser.add_argument('top', default=os.getcwd(), nargs='?',
                help='Start from directory.')
args = parser.parse_args()

top = args.top.rstrip('/')

ignore = []
for root, dirs, files in tqdm(os.walk(top, topdown=True, followlinks=False)):
    try:
        matches = parse_gitignore(root + '/.gitignore')
        
        for f in files:
            fpath = root + '/' + f
            if matches(fpath):
                ignore.append(fpath)

        newdirs = []
        for d in dirs:
            fpath = root + '/' + d
            if matches(fpath):
                ignore.append(fpath)
            else:
                newdirs.append(d)
        dirs[:] = newdirs

    except FileNotFoundError:
        pass
    except RuntimeError:
        pass

print(f"{len(ignore)} paths to ignore")

ignore = " ".join(ignore)
ignore = ignore.replace("/", "\\/")
os.system(f"sed -i 's/skippedPaths.*/skippedPaths = {ignore}/g' ~/.recoll/recoll.conf")