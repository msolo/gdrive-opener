#!/usr/bin/python3

import json
import os
import shlex
import subprocess
import sys

domain = "com.github.msolo.GDriveOpener"
docs_url = "https://docs.google.com/document/d/"
sheets_url = "https://docs.google.com/spreadsheets/d/"

def get_ns_default_string(key='', default=None):
    try:
        return subprocess.check_output(['/usr/bin/defaults', 'read', domain, key]).decode().strip()
    except:
        return default


default_command = '''open -a "Google Chrome"'''

def main():
    for f in sys.argv[1:]:
        d = json.loads(open(f).read())
        url = d.get("url")
        if not url:
            if f.endswith(".gsheet"):
                url = sheets_url + d["doc_id"]
            else:
                url = docs_url + d["doc_id"]

        exec_cmd = shlex.split(get_ns_default_string("ExecCommand", default_command))
        cmd = shlex.join(exec_cmd + [url])
        os.system(cmd)


if __name__ == "__main__":
    main()
