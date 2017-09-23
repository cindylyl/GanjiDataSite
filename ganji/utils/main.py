from .channel_extract import channel_list
from . import page_parsing
from  multiprocessing import Pool

def get_all_link(channel):
    for j in range(1,100):
        if j!='/shouji/':
            page_parsing.get_link(channel,j)

# for item in page_parsing.url_list.find():
#     page_parsing.get_info(item)

if __name__ =='__main__':
    pool=Pool()  #build process pool
    pool.map(get_all_link, channel_list)