#!/usr/bin/python3

import json
import os
import shlex
import sys

docs_url = "https://docs.google.com/document/d/"


def main():
    for f in sys.argv[1:]:
        d = json.loads(open(f).read())
        url = d.get("url")
        if not url:
            url = docs_url + d["doc_id"]
        cmd = shlex.join(["open", "-a", "Google Chrome", url])
        os.system(cmd)


if __name__ == "__main__":
    main()
