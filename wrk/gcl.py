#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

import sys
import re
import subprocess
import requests

def check_url_exists(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking URL: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <repository_path_or_url>")
        sys.exit(1)

    arg = sys.argv[1]

    # Check if argument starts with 'http'
    if arg.startswith('http'):
        url = arg
        print("===================================================== http")
    else:
        url = 'https://github.com/' + arg

    # Remove query parameters from URL
    url = re.sub(r'(\?[^\?]*)$', '', url)

    print(url)

    # Extract repository name and owner from URL
    match = re.search(r'.*/([^/]+)/([^/]+)$', url)
    if match:
        nom = f"{match.group(2)}-{match.group(1)}"
    else:
        print("Invalid URL format.")
        sys.exit(1)

    # Check if the main repository URL exists
    if not check_url_exists(url):
        print(f"Error: Repository URL {url} does not exist.")
        sys.exit(1)

    # Clone main repository
    clone_cmd = ["git", "clone", "--recursive", url, nom]
    subprocess.run(clone_cmd)

    # Handle GitHub wiki repository URL
    wiki_url = f"{url}.wiki"
#    if not check_url_exists(wiki_url):
#        print(f"Error: Wiki URL {wiki_url} does not exist.")
#        sys.exit(1)

    # Clone wiki repository
    wiki_nom = f"{nom}.wiki"
    wiki_clone_cmd = ["git", "clone", "--recursive", wiki_url, wiki_nom]
    subprocess.run(wiki_clone_cmd)

if __name__ == "__main__":
    main()

