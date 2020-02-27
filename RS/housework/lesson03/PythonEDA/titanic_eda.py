
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os

from matplotlib.font_manager import FontProperties
# 散点图
def scatter():
	# 数据准备
	N = 500
	x = np.random.randn(N)
	y = np.random.randn(N)
	# 用Matplotlib画散点图
	plt.scatter(x,y,marker='o')
	plt.show()
	# 用Seaborn画散点图
	df = pd.DataFrame({'x': x, 'y': y})
	sns.jointplot( x='x', y='y', data=df, kind='scatter')
	plt.show()


def line_cart():
	# 数据准备
	x = [1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910]
	y = [265, 323, 136, 220, 305, 350, 419, 450, 560, 720, 830]
	# 用Matplotlib画折线图
	plt.plot(x, y)
	plt.show()
	# 用Seaborn画散点图
	df = pd.DataFrame({'x': x, 'y': y})
	sns.lineplot(x, y)
	plt.show()

# 条形图
def bar_chart():
	# 数据准备
	x = ['c1', 'c2', 'c3', 'c4']
	y = [15, 18, 5, 26]
	# 用Matplotlib画条形图
	plt.bar(x, y)
	plt.show()
	# 用Seaborn画条形图
	sns.barplot(x, y)
	plt.show()


# 箱线图
def box_plots():
	# 数据准备
	# 生成0-1之间的20*4维度数据
	data = np.random.normal(loc=0.5, scale=0.15,size=(10, 4))
	print(data)
	lables = ['A', 'B', 'C', 'D']
	# 用Matplotlib画箱线图
	plt.boxplot(data, lables)
	plt.show()
	# 用Seaborn画箱线图
	df = pd.DataFrame(data=data, columns=lables)
	sns.boxplot(data=df)
	plt.show()


def pie_chart():
	# 数据准备
	nums= [25, 44, 27]
	# labels：程序员，策划,美术，
	labels = ['Programmer', 'Planner', 'Artist']
	# 用Matplotlib画饼图
	plt.pie(nums, labels=labels)
	plt.show()

# 饼图
def pie_chart2():
	# 数据准备
	data = {}
	data['Programmer'] = 25
	data['Planner'] = 33
	data['Artist'] = 37
	data = pd.Series(data)
	data.plot(kind = "pie", label='heros')
	plt.show()


#热力图
def heatmap_chart():
	# 数据准备
	np.random.seed(3)
	data = np.random.rand(3, 3)
	print(data)
	heatmap = sns.heatmap(data)
	plt.show()


#蜘蛛图
def spider_chart():
	#数据准备
	labels = np.array([u'数学', u'语文', u'英语', u'化学', u'生物'])
	values = [85, 70, 40, 78, 60]
	# 画图数据准备，角度、状态值
	angles = np.linspace(0, 2*np.pi, len(values), endpoint=False)
	stats = np.concatenate((values,[values[0]]))
	print(stats)
	angles = np.concatenate((angles, [angles[0]]))
	# 用Matplotlib画蜘蛛图
	fig = plt.figure()
	ax = fig.add_subplot(111, polar=True)
	ax.plot(angles, stats, 'o-', linewidth=2)
	ax.fill(angles, stats, alpha=0.2)
	#设置中文字体
	font = FontProperties(fname='C:\Windows\Fonts\simhei.ttf', size=14)
	ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=font)
	plt.show()


# 成对关系图
def pairplot():
	# 数据准备
	flights = sns.load_dataset('flights')
	# 用Seaborn画成对关系
	sns.pairplot(flights)
	plt.show()
# 用Seaborn画箱线图
# scatter()
# line_cart()
# bar_chart()
# box_plots()
# pie_chart2()
# heatmap_chart()
# spider_chart()
pairplot()