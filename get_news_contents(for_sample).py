import data.tools as tools
from tqdm import tqdm
import pandas as pd
#저장된 링크 제목과 본문 가져오기

links=pd.read_csv("./save/links.csv")
file=links.link
#샘플 갯수 선택
file=file[:10]

title=[]
content=[]

for link in tqdm(file):
    text=tools.get_title_contents(link)
    if text!=None:
        title.append(text["title"])
        content.append(text["contents"])

        
df = pd.DataFrame({
    'title': title,
    'content':content
})


df.to_csv("./save/sample.csv",encoding="UTF-8",index=False)
