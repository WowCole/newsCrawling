import data.tools as tools
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import data.tools as tools

# daum="https://news.daum.net"
# soup=tools.soup_page(daum)

# count=10

# articles=[]
# for i in range(count):
#     article={ 
#         "link":soup.select(".item_issue > a")[i].get("href"),
#         "logo":soup.select(".item_issue > a >img")[i].get("src"),
#         "thumbnail":soup.select(".logo_cp >img")[i].get("src"),
#         "category":soup.select(".txt_category")[i].text,
#         "title":soup.select(".link_txt")[0].text.strip()
#     }
#     articles.append(article)

# with open("./save/dailyCrawling.json", 'w',encoding="UTF-8") as outfile:
#     json.dump(articles, outfile)
    
print(tools.get_title_contents("https://n.news.naver.com/mnews/article/119/0002656834?sid=100"))
print(tools.daily_news_grab())