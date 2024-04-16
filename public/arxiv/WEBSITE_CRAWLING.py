"""
-*- coding: utf-8 -*-
@author: Wang Zhaohui
"""

import os
import time
import xlwt
import requests
from bs4 import BeautifulSoup

# crawler initialize
os.chdir('/Users/gxq/arxiv')
header = {
    'Host': 'arxiv.org',
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
        'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

# initialize ".txt" and ".xls" document to save data
with open('arxiv_text_updated.txt', 'w', encoding="utf-8") as data:
    nothing_happen = 0
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('My Worksheet', cell_overwrite_ok=True)
worksheet.write(0, 0, "No.")
worksheet.write(0, 1, "arXiv")
worksheet.write(0, 2, "Title")
worksheet.write(0, 3, "First Author")
worksheet.write(0, 4, "Abstract")

# website crawling part
num_count = 0
def output(url_name, url_name_turn):
    print('begin')
    # initialize website crawling set
    global num_count
    url = url_name
    time.sleep(3)
    r1 = requests.get(url, headers=header)
    soup = BeautifulSoup(r1.content, 'lxml')
    text_dl = soup.select('div#dlpage > h3')
    total = soup.find('small')
    text_ds = text_dl[0].get_text()
    text_d = text_ds.split()
    date = text_d[0]
    total = int(total.text.split()[3])
    page, rest = divmod(total, 25)
    list_page = range(1, page + 1)

    # get information deposited in lists
    def get_all_this_page(url):

        header = {
            'Host': 'arxiv.org',
            'Accept':
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                'application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        time.sleep(3)
        rr = requests.get(url, headers=header)
        soup2 = BeautifulSoup(rr.content, 'lxml')
        linkall0 = soup2.select('div#dlpage > dl > dt > span > a:nth-child(1)')
        titleall0 = soup2.select('div#dlpage > dl > dd > div > div.list-title.mathjax')
        number0 = soup2.select('div#dlpage > dl > dt > a')
        author0 = soup2.select('div#dlpage > dl > dd > div > div.list-authors > a:nth-of-type(1)')

        return linkall0, titleall0, number0, author0

    # filter information
    linkall = []
    titleall = []
    number = []
    author = []

    fir = get_all_this_page(url)
    linkfir = fir[0]
    titlefir = fir[1]
    numberfir = fir[2]
    authorfir = fir[3]

    try:
        for i in range(0, 25):
            linkall.append(linkfir[i].get('href'))
            titleall.append(titlefir[i].get_text())
            number.append(numberfir[i].get_text())
            author.append(authorfir[i].get_text())
    except:
        nothing = 'happened'

    # get information in other pages
    fir_page = int(number[0].split('[')[1].split(']')[0])
    for j in list_page:
        urlmid = url_name_turn + str(
            j * 25) + '&show=25'
        mid = get_all_this_page(urlmid)
        linkmid = mid[0]
        titlemid = mid[1]
        numbermid = mid[2]
        authormid = mid[3]

        if j < page:
            for j_1 in range(0, 25):
                linkall.append(linkmid[j_1].get('href'))
                titleall.append(titlemid[j_1].get_text())
                number.append(numbermid[j_1].get_text())
                author.append(authormid[j_1].get_text())
        else:
            for j_2 in range(0, rest):
                linkall.append(linkmid[j_2].get('href'))
                titleall.append(titlemid[j_2].get_text())
                number.append(numbermid[j_2].get_text())
                author.append(authormid[j_2].get_text())

    abstract = []
    for i in range(0, total):
        abstract.append(get_abstract(linkall[i][5:]))
    for k in range(0, total):
        link = 'arXiv:' + linkall[k][5:]
        linkall[k] = link
        auth = "First Author:" + author[k]
        author[k] = auth

    # save information
    with open('arxiv_text_updated.txt', 'a', encoding="utf-8") as data:
        num_count_excel = num_count
        for n in range(0, total):
            num_count_excel += 1
            worksheet.write(num_count_excel, 0, num_count_excel)
            worksheet.write(num_count_excel, 1, linkall[n])
            worksheet.write(num_count_excel, 2, titleall[n])
            worksheet.write(num_count_excel, 3, author[n])
            worksheet.write(num_count_excel, 4, abstract[n])

        for m in range(0, total):
            num_count += 1
            data.write('[' + str(num_count) + ']' + '\n')
            data.write(linkall[m])
            data.write(titleall[m])
            data.write(author[m] + '\n')
            data.write(abstract[m])
            data.write('\n')


# get abstract by each arXiv code
def get_abstract(code):

    time.sleep(3)
    url2 = "https://arxiv.org/abs/" + str(code)
    rr2 = requests.get(url2, headers=header)
    soup = BeautifulSoup(rr2.content, 'lxml')
    abstract = soup.select('div#abs > blockquote')
    text = []
    for i in abstract:
        text.append(i.get_text())
    text = str(text)[4:-10]

    return text


def main():
    url_1 = 'https://arxiv.org/list/cs.CY/recent'
    url_1_t = 'https://arxiv.org/list/cs.CY/pastweek?skip='
    url_2 = 'https://arxiv.org/list/cs.SI/recent'
    url_2_t = 'https://arxiv.org/list/cs.SI/pastweek?skip='
    url_3 = 'https://arxiv.org/list/cs.IR/recent'
    url_3_t = 'https://arxiv.org/list/cs.IR/pastweek?skip='
    url_4 = 'https://arxiv.org/list/cs.CE/recent'
    url_4_t = 'https://arxiv.org/list/cs.CE/pastweek?skip='

    output(url_1, url_1_t)
    #output(url_2, url_2_t)
    #output(url_3, url_3_t)
    #output(url_4, url_4_t)

    workbook.save('/Users/gxq/arxiv/arxiv_data_updated.xls')

    print('Complete')


main()
