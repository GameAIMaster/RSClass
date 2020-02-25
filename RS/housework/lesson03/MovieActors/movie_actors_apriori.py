import pandas as pd
import time
from mlxtend.frequent_patterns import apriori, association_rules
#数据加载
data = pd.read_csv("movie_actors.csv")
start = time.time()
# 进行one-hot编码（离散值有多少取值，就用多少维来表示这个特征）
data_hot_encode = data.drop('actors', 1).join(data.actors.str.get_dummies('/'))
pd.options.display.max_columns = 100
print(data_hot_encode.head())

# 将movieId, title设置为index
data_hot_encode.set_index(['title'], inplace=True)
print(data_hot_encode.head())
frequent_items = apriori(data_hot_encode, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_items, metric='lift', min_threshold=0.5)
print('频繁项集：', frequent_items)
print('关联规则：', rules)
end = time.time()
print('计算用时：%s' % (end - start))
