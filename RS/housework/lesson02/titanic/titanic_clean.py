import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# 特征提取
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer




train_path = 'train.csv'
train_df = pd.read_csv(train_path, header=0)
# 数据探索
print('查看数据信息，列名、非空个数、类型等')
print('-'*30)
print('查看数据摘要')
print()
print('-'*30)
print('查看数据离散分布')
print()
print('-'*30)
print('查看前5条数据')
print()
print('-'*30)
print('查看后5条数据')
print()

# 使用平均年龄填充年龄中的nan值


# 使用票价平均值填充年龄中的nan值


# 使用登录最多的港口田中登录港口的nan值


# 特征选择

print('特征值')
print()


print()
# 构造ID3决策树

# 决策树训练

# 决策树预测

# 得到决策树准确率(基于训练集)

# 使用K折交叉验证 统计决策树的准确率