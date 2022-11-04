from selenium import webdriver
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time
import getpass
import urllib.request
from bs4 import BeautifulSoup
import os
import undetected_chromedriver as uc
from cgitb import text
from importlib.resources import read_text
import pandas as pd
import news_sites as ns
import which_site as ws

driver = uc.Chrome()
news_site = input()

class_name=ws.find_site(news_site)


driver.get(news_site)

title_text = driver.find_element(By.CLASS_NAME,class_name[0]).text

contents_text = driver.find_element(By.CLASS_NAME,class_name[1]).text

print(title_text,contents_text)