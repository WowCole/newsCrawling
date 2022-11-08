import urllib.request
from bs4 import BeautifulSoup
import os
from importlib.resources import read_text
import requests
import data.tools as tools

print(tools.get_title_contents(input()))