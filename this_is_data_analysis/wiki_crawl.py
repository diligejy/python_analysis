# -*- coding : utf-8 -*-
% matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re

source_url = 'https://namu.wiki/RecentChanges'

#
req = requests.get(source_url)
html = req.content 
soup = BeautifulSoup(html, 'lxml')
contents_table = soup.find(name = 'table')
table_body = contents_table.find(name = 'tbody')
table_rows = table_body.find_all(name = "tr")

#
page_url_base = 'https://namu.wiki'
page_urls = []
for index in range(0, len(table_rows)):
    first_td = table_rows[index].find_all('td')[0]
    td_url = first_td.find_all('a')
    if len(td_url) > 0:
        page_url = page_url_base + td_url[0].get('href')
        page_urls.append(page_url)

# 중복 url 제거
page_urls = list(set(page_urls))

