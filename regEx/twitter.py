import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE): # removes everything before the username
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) # removes everything before the username
    print(f"Username:", matches.group(1))