from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 加载数据
data = pd.read_csv("team_cluster_data.csv", encoding='gbk')
train_x = data[["2019国际排名", "2018世界杯排名", "2015亚洲杯排名"]]
# 准备数据：数据预处理
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
print(train_x)
# 分割数据，将25%的数据作为测试集，其余的作为训练集

# 选择模型Kmeans
kmeans = KMeans(n_clusters=3)

# 训练模型
kmeans.fit(train_x)

# 评估

# 超参数调整
# 预测
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原始数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类结果'}, axis=1, inplace=True)
print(result)
# 将结果导出到CSV文件
#result.to_csv("team_cluster_data.csv")