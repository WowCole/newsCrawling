from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup as bs
import data.publisher as pb
import data.temp as temp
import datetime
# dates = date_range("20210101", "20210109")

# 날짜 범위 계산
def date_range(start, end):
    start = datetime.strptime(start, "%Y%m%d")
    end = datetime.strptime(end, "%Y%m%d")
    dates = [(start + timedelta(days=i)).strftime("%Y%m%d") for i in range((end-start).days+1)]
    return dates

#페이지 수 계산
def soup_page(url):
    import requests
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    req = requests.get(url,headers=headers)
    html=req.text
    soup = bs(html, 'html.parser')
    return soup

#제목, 본문 가져오기
def find_site(url):
    for i in range(len(pb.news)):
        if pb.news[i]["name"] in url:
            return pb.news[i]


def get_title_contents(news_site):
    try:
        news_info={}
        class_name=find_site(news_site)
        soup=soup_page(news_site)
        #title
        news_info["title"] = soup.select_one(class_name["title"]).text

        if class_name["name"]=="naver":
            #time
            temp_time=soup.select_one(class_name["time"][0]).get(class_name["time"][1])
            date_time_str = temp_time
            news_info["time"]=datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
            #press
            news_info["press"]=soup.select_one(class_name["press"][0]).get(class_name["press"][1])
            #contents
            contents_text = str(soup.select_one(class_name["contents"]))
            contents_text=[i for i in contents_text.split("<br/>") if len(i) >1 and "class=" not in i and "id="not in i and "span" not in i and "strong" not in i]
        elif class_name["name"]=="daum":
            #time
            temp_time=soup.select_one(class_name["time"]).text+":00"
            date_time_str = temp_time
            news_info["time"]=datetime.datetime.strptime(date_time_str, '%Y. %m. %d. %H:%M:%S')
            # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y. %m. %d. %H:%M:%S')
            # news_info["time"]=date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
            #press
            news_info["press"]=soup.select_one(class_name["press"][0]).text
            #contents
            contents_text=soup.select(class_name["contents"])
            contents_text= [i.text.strip() for i in contents_text]
        new_news=[]
        remover=["\n","\t","</div>","\'"]
        for i in range(len(contents_text)):
            line=contents_text[i].strip()
            for j in remover:
                line=line.replace(j,"")
            new_news.append(line)
        seperator=","
        news_info["contents"]=seperator.join(new_news).replace(","," ")


        #img
        news_info["img"]=soup.select_one(class_name["img"][0]).get(class_name["img"][1])
        
       
        #reporter
        news_info["reporter"]=soup.select_one(class_name["reporter"]).text[:3]
    except AttributeError as err:
        return None
    else:
        return news_info

# 매일 크롤링
def daily_news_grab():
    daum="https://news.daum.net"
    soup=soup_page(daum)
    count=10
    links=[soup.select(".item_issue > a")[i].get("href") for i in range(count)]
    articles=[get_title_contents(i)for i in links]
    for i in range(len(articles)):
        articles[i]["link"]=links[i]
    return articles

def check_page(url):
    try:
        soup=soup_page(url)
        news_lists=soup.find(class_="type06_headline").find_all('a')+soup.find(class_="type06").find_all('a')
       
    except AttributeError as err:
        return None
    else:
        page_length=len(soup.select('.paging > a'))
        for count in range(page_length):
            new_soup=soup_page(url+f"&page={count+1}")
            new_news_lists=new_soup.find(class_="type06_headline").find_all('a')+soup.find(class_="type06").find_all('a')
            for i in grab_link(new_news_lists):
                temp.link.append(i)
        return 


#페이지 수 확인
def grab_link(link):
    news_lists_links=list(set([link[i].get('href')for i in range(len(link))]))
     #기사 리스트 유무
    return news_lists_links
