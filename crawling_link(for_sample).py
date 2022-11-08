import urllib.request
from bs4 import BeautifulSoup as bs
import os
from importlib.resources import read_text
import requests
import data.tools as tools
import data.publisher as publisher
import data.setting as setting
import data.temp as temp
from tqdm import tqdm
import sys
import pandas as pd

#네이버 기본 링크 생성
dateRange=setting.dateRange
category_code =setting.category_code

naver = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2="

category_url = [f"{naver+str(category)}" for category in category_code]

category_url_date =[]
for url in category_url:
    for date in dateRange:
        category_url_date.append(url+"&date="+date)

for link in tqdm(category_url_date):
    tools.check_page(link)

#기간별 전체 뉴스 링크 저장
temp_link=pd.DataFrame({
    "link":temp.link
})
temp_link.to_csv("./save/links.csv",encoding="UTF-8",index=False)






