import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
pd.options.display.max_columns = 100
movies = pd.read_csv('movies.csv')

# 将title设置为Index
one_hot_encode_movies = movies.set_index(['movieId', 'title'])
# 对数据进行one_hot编码
one_hot_encode_movies = one_hot_encode_movies.drop('genres', 1).join(one_hot_encode_movies.genres.str.get_dummies(sep='|'))

# 挖掘频繁项集
itemsets = apriori(one_hot_encode_movies, min_support=0.02, use_colnames=True)
# 按照支持度从大到小排序
itemsets = itemsets.sort_values(by='support', ascending=False)
print('频繁项集：')
print(itemsets)
rules = association_rules(itemsets, metric='lift', min_threshold=2)
# 按照提升度从大到小排
rules = rules.sort_values(by='lift', ascending=False)
print('关联规则：')
print(rules)
