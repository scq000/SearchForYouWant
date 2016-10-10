#! /usr/bin/env python
# ! coding=utf-8
# ! author scq000

import requests
import sys
import re
import urllib
from bs4 import BeautifulSoup

#  http://www.btydt.com/s?kw=key1+key2&pn=1
def searchBTYDY(keyword):
    global max
    result = []
    req = requests.get(url="http://www.btydt.com/s", params={ 'kw' : keyword, 'pn': 1} ,timeout=20)
    # 总共搜索的条数
    search_tip = BeautifulSoup(req.content).find_all(class_="search_tip")[0].get_text()
    itemsCount = int(re.findall(r'\b\d+\b', search_tip)[0])

    result = filter(req)

    currentpage = 1
    while(len(result) < itemsCount):
        if(max_page and currentpage >= max_page):
            break
        currentpage = currentpage + 1
        req = requests.get(url="http://www.btydt.com/s", params={ 'kw' : keyword, 'pn': currentpage}, timeout=20)
        result  += filter(req)

    return result

# 过滤出magnet thurnder 等有用信息
def filter(req):
    soup = BeautifulSoup(req.content)
    files = []
    tempFile = {'name': '', 'link': '', 'magnet': ''}
    for i, item in enumerate(soup.select(".item > a")):
        tempFile['name'] = item.get_text()
        tempFile['link'] = link = item['href'][1:]
        # 获取magnet地址
        magnetReq = requests.get('http://www.btydt.com' + link)
        beautiful_soup = BeautifulSoup(magnetReq.content)
        tempFile['magnet'] = beautiful_soup.find('a', text="磁力链接")['href']
        tempFile['thurder'] = beautiful_soup.find('a', text="迅雷下载")['href']
        tempFile['updateTime'] = beautiful_soup.select('#details > p')[3].get_text()
        tempFile['size'] = beautiful_soup.select('li > .size')[0].get_text()
        # print tempFile['magnet']
        files.append(tempFile)
        tempFile = {}

    return files


#http://www.diaosisou.com/list/%E4%BA%91%E7%94%BB%E7%9A%84%E6%9C%88%E5%85%89/1
def searchDiaosisou(keyword):
    result = []
    req = requests.get('http://www.diaosisou.com/list/' + keyword + '/1', timeout= 10)
    search_tip = BeautifulSoup(req.content).find(class_="rststat").get_text()
    itemsCount = int(re.findall(r'\b\d+\b', search_tip)[0])

    result = filterDiaosisou(req)

    currentpage = 1
    while(len(result) < itemsCount):
        if(max_page and currentpage >= max_page):
            break
        currentpage = currentpage + 1
        req = requests.get(url="http://www.diaosisou.com/list/" + keyword + '/' + str(currentpage) ,timeout=20)
        result  += filterDiaosisou(req)

    return result

def filterDiaosisou(req):
    soup = BeautifulSoup(req.content)
    files = []
    tempFile = {'name': '', 'magnet': ''}
    # print soup.find_all(class_="mlist")[0]

    for item in soup.select(".mlist > li"):
        tempFile['name'] = item.find("a").get_text().replace('<span class="mhl">', '').replace('</span>', '').replace('\n', ' ')
    #     # 获取magnet地址

        tempFile['magnet'] = item.find("a", text="[磁力链接] ")['href']
        tempFile['thurder'] = item.find("a", text="[迅雷链接]")['href']
        tempFile['info'] = item.find(class_='BotInfo').get_text()
        files.append(tempFile)
        tempFile = {}
    return files

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')

    keyword = sys.argv[1]
    # 设置最大页数
    max_page = 10
    # result = searchBTYDY(keyword)
    # searchDiaosisou('云画的月光')
    result = searchDiaosisou(keyword)
    for i,item in enumerate(result):
        print str(i) + '--->' + item['name']
        # print item['updateTime']
        # print '大小:' + item['size']
        print item['magnet']
        print item['thurder']
        print item['info']
        print '\n'