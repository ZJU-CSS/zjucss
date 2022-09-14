"""
-*- coding: utf-8 -*-
@author: Wang Zhaohui
Updated at 09:01 on May 10th
"""

import xlrd
import time
import plotly
import random
import plotly.express as px
#from pynput.mouse import Button, Controller

# get data from ".xls" document
data = xlrd.open_workbook('/Users/xxxxxxqq/vscodeProjects/arxiv/arxiv_data_updated.xls')
table = data.sheet_by_index(0)
num = table.nrows - 1
nrows = table.nrows
arxiv_lst_graph = []
author_lst_graph = []
for row in range(1, nrows):
    arxiv = table.cell(row, 1).value[6:]
    arxiv_lst_graph.append(arxiv)
    author = table.cell(row, 3).value[13:]
    author_lst_graph.append(author)
x1 = author_lst_graph[:]
x2 = []
no_list = []
arxiv_lst = []
title_lst = []
author_lst = []
abstract_lst = []
for row in range(1, nrows):
    no = table.cell(row, 0).value
    no_list.append(no)
    arxiv = table.cell(row, 1).value
    arxiv_lst.append(arxiv)
    title = table.cell(row, 2).value[1:]
    title_lst.append(title)
    author = table.cell(row, 3).value
    author_lst.append(author)
    abstract = table.cell(row, 4).value[:700]+"...."
    abstract_lst.append(abstract)
for i in range(11):
    arxiv_lst.append("")
    title_lst.append("")
    author_lst.append("")
    abstract_lst.append("")
temp = []
for i in title_lst:
    list_i = list(i)
    if len(list_i) >= 80:
        list_i.insert(80,"<br>")
    temp.append("".join(list_i))
title_lst = temp[:]
temp = []
for i in abstract_lst:
    i = i.replace('\\n','<br />')
    temp.append(i)
abstract_lst = temp[:]
merge_lst = []
count = 0
for i in author_lst:
    j = abstract_lst[count]
    k = title_lst[count]
    merge_lst.append([i, j, k])
    count += 1

# optimize the data structure which will be used in sunburst graph
for i in range(num//7):
    x2.append(' ')
    x2.append('  ')
    x2.append('   ')
    x2.append('    ')
    x2.append('     ')
    x2.append('      ')
    x2.append('       ')
for i in range(num-(num//7)*7):
    x2.append(' ')
x1.append(' ')
x1.append('  ')
x1.append('   ')
x1.append('    ')
x1.append('     ')
x1.append('      ')
x1.append('       ')
for i in range(2):
    x2.append("         ")
for i in range(2):
    x2.append("          ")
for i in range(3):
    x2.append("           ")
x1.append("         ")
x2.append("Weekly papers<br>(ZJUCSS)")
x1.append("          ")
x2.append("Weekly papers<br>(ZJUCSS)")
x1.append("           ")
x2.append("Weekly papers<br>(ZJUCSS)")
x1.append("Weekly papers<br>(ZJUCSS)")
x2.append("")

# visualize process
data = dict(
    character=x1,
    parent=x2,
    value=[random.randrange(0,50) for i in range(num+11)])
fig =px.sunburst(
    data,
    names='character',
    values='value',
    parents='parent')    #color='parent'
template = "plotly_dark"
fig.update_layout(template=template,title='the Latest Weekly Papers on arXiv')
fig.update_traces(marker_colorscale='Reds')  # Maybe Reds or Greens
fig.update_traces(hovertemplate='<b>%{customdata}</b><br><b>%{meta[2]}</b><br><b>%{meta[0]}</b><br><b>%{meta[1]}</b><extra></extra>',
    meta=[merge for merge in merge_lst], customdata=[no for no in arxiv_lst],)
# fig.show()
plotly.offline.plot(fig, filename='/Users/xxxxxxqq/vscodeProjects/arxiv/arxiv_data_graph.html')



