import urllib.request
from bs4 import BeautifulSoup
import os
from importlib.resources import read_text
import requests
import data.tools as tools
#네이버 기사 혹은 다음 기사 링크 인풋
print(tools.get_title_contents(input()))