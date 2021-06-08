# -*- coding: utf-8 -*-

import csv
import random
import requests
from lxml import etree
from loguru import logger

UA_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36Edge/13.10586",
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko)Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27'
    'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
]

headers = {
    "User-Agent": random.choice(UA_LIST)
}
url_list = []

with open("pkg_url_new.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] != "URL":
            url_list.append(row[1])

with open("url.txt", "r", encoding="utf8") as f:
    already_crawl_url_list = [url.strip('\n') for url in f.readlines()]

for index, url in enumerate(url_list):
    if not url.startswith("http"):
        url = f"http://{url}"
    if not url.startswith("http:"):
        url = url.replace("http", "http:")
    if url in already_crawl_url_list:
        continue
    logger.info(f"is accessing {index + 1} th link ------------> {url}")
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        continue
    xpathor = etree.HTML(response.text)
    try:
        try:
            commit_num = xpathor.xpath('//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/div/div/div/ul/li/a/span/strong/text()')[0]
        except IndexError as e:
            commit_num = "".join(re.findall(r"\d+", xpathor.xpath('//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[3]/div/div/div/ul/li/a/span/strong/text()')[0]))
        with open("commits.txt", "a", encoding="utf8") as f:
            f.write(f"{url} {commit_num}\n")
    except Exception:
        pass
    with open("url.txt", "a", encoding="utf8") as f:
        f.write(f"{url}\n")
