import pandas as pd
import time
from mlxtend.frequent_patterns import apriori, association_rules
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

#数据加载
data = pd.read_csv("Market_Basket_Optimisation.csv", header=None, sep='/')
start = time.time()
# print(data.head())
# 进行one-hot编码（离散值有多少取值，就用多少维来表示这个特征）
data_hot_encode = data.drop(0, 1).join(data[0].str.get_dummies(','))
pd.options.display.max_columns = 100
# print(data_hot_encode.head())
frequent_items = apriori(data_hot_encode, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_items, metric='lift', min_threshold=0.5)
# 按照提升度从大到小进行排序
rules = rules.sort_values(by="lift" , ascending=False)
print('频繁项集：', frequent_items)
print('-'*20, '关联规则', '-'*20)
print(rules)
print('关联规则：', rules)
end = time.time()
print('计算用时：%s' % (end - start))

# 去掉停用词
def remove_stop_words(f):
	stop_words = ['Movie']
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("MarketBasket.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()


# 读取title 和 genres字段
word = " ".join(data[0])
create_word_cloud(word)
