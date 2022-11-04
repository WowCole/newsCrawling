import news_sites as ns

def find_site(url):
    for i in range(len(ns.news)):
        if ns.news[i]["name"] in url:
            title= ns.news[i]["title"]
            contents=ns.news[i]["contents"]
            return [title,contents]
