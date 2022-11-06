from selenium import webdriver

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
from bs4 import BeautifulSoup
import os
from importlib.resources import read_text
import news_sites as ns
import which_site as ws
import requests

news_site = input()

class_name=ws.find_site(news_site)
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
req = requests.get(news_site,headers=headers)
html=req.text
soup = BeautifulSoup(html, 'html.parser')


title_text = soup.select_one(
    class_name[0]
    ).text

contents_text = soup.select_one(
    class_name[1]
    ).text

print(title_text,contents_text)