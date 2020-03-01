# coding: utf-8
# 手肘法
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib as plt

# 输入数据
data = pd.read_csv("team_cluster_data.txt")
train_x= data[["2019国际排名", "2018世界杯排名", "2015亚洲杯排名"]]


# 规范化到[0,1]之间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
print(train_x)
# 统计不同的K取值的误差平方和
sse = []
for k in range(1,11):
    # kmeans 算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    # 计算 inertia簇内误差平方和
    sse.append(kmeans.inertia_)
# x = range(1, 11)
# plt.xlabel('K')
# plt.ylabel('SSE')
# plt.plot(x, sse, 'o-')
# plt.show()

# K 增大到一定程度时，K增大对SSE减小的作用越小
# 这里K值设置成3
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
print(pd.DataFrame(predict_y))
# 合并聚类，插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
# 将0重命名为聚类结果
result.rename({0: u'聚类结果'}, axis=1, inplace=True)
print(result.head())
