from bs4 import BeautifulSoup
import requests
import time
import pymongo

client=pymongo.MongoClient('localhost',27017)
test=client['test']
phone_number=test['phone_number']

header={'User-Agent':'xxxx',
        'Cookie':'xxxxxx'
        }
def get_info(page,header):
    url='http://bj.58.com/shoujihao/pn{}/'.format(str(page))
    source=requests.get(url,headers=header)
    time.sleep(2)
    soup=BeautifulSoup(source.text,'lxml')
    if soup.select('div.infocont b')[0].text =='0':
        pass
    else:
        names=soup.select('.number')
        links=soup.select('a.t')

        for name, link in zip(names,links):
            data={
                'name':name.text,
                'link':link.get('href')
            }
            phone_number.insert_one(data)


#get_info(1)
for i in range(120):
    get_info(i,header)
    print('done')