import requests
from bs4 import BeautifulSoup
import time
import pymongo

client=pymongo.MongoClient('localhost',27017)
test=client['test']
url_list=test['url_list']
info_list=test['info_list']

def get_link(channel,page,who=0):
    url='http://bj.58.com{}{}/pn{}/'.format(channel,str(who),str(page))
    source=requests.get(url)
    time.sleep(2)
    soup=BeautifulSoup(source.text,'lxml')
    if soup.find('td','t'):
        links=soup.select('a.t')
        for i in links:
            link=i.get('href')
            if 'zhuanzhuan' not in link and 'jump' not in link and 'adJump' not in link:
                real_link=link.split('?')[0]
                url_list.insert_one({'url':real_link})
                #print(real_link)
    else:
        pass #nothing

def get_info(url):
    source=requests.get(url)
    time.sleep(1)
    soup=BeautifulSoup(source.text,'lxml')
    title=soup.select('div.col_sub h1')[0].text
    price=soup.select('span.price')[0].text
    date=soup.select('li.time')[0].text
    area=list(soup.select('span.c_25d')[1].stripped_strings) if soup.find_all('span','c_25d') else None
    data={'title':title,'price':price,'date':date,'area':area}
    info_list.insert_one(data)
    #print(data)

#get_link('/pbdn/',100)

#get_info('http://bj.58.com/shouji/25589947839045x.shtml')

