# -*- coding: utf-8 -*-
# 用PageRank挖掘希拉里邮件中的重要人物关系
import pandas as pd
import networkx as nx
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 10, 'display.max_columns', 10)
# 数据加载
emails = pd.read_csv("Emails.csv")
# 读取别名文件
file = pd.read_csv("Aliases.csv")
aliases={}
for index, row in file.iterrows():
    aliases[row['Alias']] = row['PersonId']
# 读取人名文件
file = pd.read_csv("Persons.csv")
persons = {}
for index,row in file.iterrows():
    persons[row['Id']] = row['Name']
#数据探索
# print(emails.head())
# print(file.head())
# for row in zip(emails.MetadataTo, emails.MetadataFrom, emails.RawText):
#     print(row)
#     print(('H', 'Sullivan, Jacob J') in row)
#     break


# 针对别名进行转换
def unity_name(name):
    # 姓名统一用小写
    name = str(name).lower()
    # 去掉， 和@后面的内容
    name = name.replace(',', '').split('@')[0]
    # 别名转换
    if name in aliases.keys():
        return persons[aliases[name]]
    return name


def show_graph(graph, type='spring_layout'):
    if type=='spring_layout':
        # 使用Spring Layout布局，类似中心放射状
        postion = nx.spring_layout(graph)
    elif type=='circular_layout':
        # 使用Circular Layout布局，在一个圆环上均匀分布
        postion = nx.circular_layout(graph)
    # 设置网络图中的节点大小，大小与pagerank值有关，因为pagerank值很小，所以需要*20000
    nodeSize = [(x['pagerank']*20000) for v, x in graph.nodes(data=True)]
    # 设置网络图中的边长
    edgeSize = [np.sqrt(e[2]['weight']) for e in graph.edges(data=True)]
    # 绘制节点
    nx.draw_networkx_nodes(graph, postion, node_size=nodeSize, alapha=0.4)
    # 绘制边
    nx.draw_networkx_edges(graph, postion, edge_size=edgeSize, alapha=0.2)
    # 绘制节点的label
    nx.draw_networkx_labels(graph,postion,font_size=10)
    # 输出希拉里邮件中的所有人物关系
    plt.show()
# 将寄件人和收件人的姓名进行规范化
emails.MetadataFrom = emails.MetadataFrom.apply(unity_name)
emails.MetadataTo = emails.MetadataTo.apply(unity_name)
# 设置边的权重的与发件的次数
edges_weight_temp = defaultdict(list)
for row in zip(emails.MetadataTo, emails.MetadataFrom, emails.RawText):
    temp = (row[0], row[1])
    if temp not in row:
        edges_weight_temp[temp] = 1
    else:
        edges_weight_temp[temp] += 1
print(edges_weight_temp)
print('-'*100)
# 转化格式(from, to), weight=> from, to, weight
edges_weight = [(k[0], k[1], value) for k, value in edges_weight_temp.items()]
# 创建一个有向图
graph = nx.DiGraph()
# 设置有向图的路径及权重
graph.add_weighted_edges_from(edges_weight)
# 计算每个节点的PR值，并作为几点的pagerank属性
pagerank = nx.pagerank(graph)
# 获取每个节点的PageRank数值
pagerank_list = {node: rank for node, rank in pagerank.items()}
print(pagerank_list)
# 将PageRank数值作为节点的属性
nx.set_node_attributes(graph, name='pagerank', values=pagerank_list)
# 画网络图
show_graph(graph)

# 将完整的图谱进行精简
# 设置PR值的阈值，筛选大于阈值的重要核心节点
pagerank_threshold = 0.005
# 复制一份计算好的网络图
small_graph = graph.copy()
# 剪掉PR值小于pagerank_threshold的节点
for n, p_rank in graph.nodes(data=True):
    if p_rank['pagerank'] < pagerank_threshold:
        small_graph.remove_node(n)
# 画网络图
show_graph(small_graph, 'circular_layout')

