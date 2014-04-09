#!/usr/bin/python

from bs4 import BeautifulSoup
from pprint import pprint
import re

with open("servers.html") as f:
    html = f.read()

soup = BeautifulSoup(html)

for table in soup.find_all("table"):
    for tr in table.find_all("tr"):
        for td in tr.find_all("td"):
            try:
                content = td.get_text()
                if re.match("^[a-z0-9\.]+\.[a-z]+$", content):
                    print content
            except:
                pass
