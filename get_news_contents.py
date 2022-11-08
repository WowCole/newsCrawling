import data.tools as tools
from tqdm import tqdm
import pandas as pd

file = open('./save/newslinks.txt', mode='r', encoding='UTF-8').read().split(",")
file=file[:5000]

title_content_1=[]
title_content_2=[]

for link in tqdm(file):
    text=tools.get_title_contents(link)
    if text!=None:
        title=text[0]
        content=text[1]
        title_content_1.append(title)
        title_content_2.append(content)


df = pd.DataFrame({
    'title': title_content_1,
    'content':title_content_2
})


df.to_csv("./save/sample.csv",encoding="UTF-8",index=False)
