import requests
from lxml import etree

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'}

ori_url = 'http://cq.58.com/sale.shtml'
first_url = 'http://cq.58.com'

def get_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    last_urls = selector.xpath('//*[@id="ymenu-side"]/ul/li/span[1]/a/@href')
    for last_url in last_urls:
        channel_url = first_url + last_url
        print(channel_url)

get_url(ori_url)

channel_list = '''
    http://cq.58.com/shouji/
    http://cq.58.com/tongxunyw/
    http://cq.58.com/danche/
    http://cq.58.com/diandongche/
    http://cq.58.com/diannao/
    http://cq.58.com/shuma/
    http://cq.58.com/jiadian/
    http://cq.58.com/ershoujiaju/
    http://cq.58.com/yingyou/
    http://cq.58.com/fushi/
    http://cq.58.com/meirong/
    http://cq.58.com/yishu/
    http://cq.58.com/tushu/
    http://cq.58.com/wenti/
    http://cq.58.com/kaquan/
    http://cq.58.com/chengren/
'''
