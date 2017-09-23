import requests
from bs4 import BeautifulSoup


url='http://bj.58.com/sale.shtml'
#pre_link='http://bj.58.com'
source=requests.get(url)
soup=BeautifulSoup(source.text,'lxml')
channel_list=[]

for item in soup.select('span.dlb a'):
    if item.get('href') != None:
        link=item.get('href')
        channel_list.append(link)



'''
http://bj.58.com/shouji/
http://bj.58.com/shoujihao/
http://bj.58.com/danche/
http://bj.58.com/zixingche/
http://bj.58.com/diannao/
http://bj.58.com/shuma/
http://bj.58.com/jiadian/
http://bj.58.com/ershoujiaju/
http://bj.58.com/bangong/
http://bj.58.com/ershoushebei/
http://bj.58.com/yingyou/
http://bj.58.com/fushi/
http://bj.58.com/meirong/
http://bj.58.com/yishu/
http://bj.58.com/tushu/
http://bj.58.com/wenti/
'''