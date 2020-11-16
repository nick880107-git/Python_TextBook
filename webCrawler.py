import requests
from bs4 import BeautifulSoup
def getData(url):
    my_cookies={"over18":'1'}
    res=requests.get(url,cookies=my_cookies)
    # headers={"cookie":"over18=1"}
    # res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,"html.parser")

    target=soup.findAll("div",{'class':'title'})
    for targets in target:
        if targets.text!=None:
            print(targets.text)

    next_link=soup.find("a",string="‹ 上頁")
    print(next_link["href"])
    return next_link["href"]

url="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    url="https://www.ptt.cc"+getData(url)
    count+=1
