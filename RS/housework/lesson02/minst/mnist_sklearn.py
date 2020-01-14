# -*- coding: utf-8 -*-
# 使用多种分类器进行Mnist手写分类
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from sklearn import svm #SVM
from sklearn.linear_model import LogisticRegression#逻辑回归
from sklearn.tree import DecisionTreeClassifier #决策树
from sklearn.naive_bayes import GaussianNB,MultinomialNB, BernoulliNB #高斯朴素贝叶斯
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.ensemble import AdaBoostClassifier #AdaBoost
from xgboost import XGBClassifier #XGBoost
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pylab as plt

# 加载数据
digits = load_digits()
data = digits.data
# 数据探索
print(data.shape)
# 查看第一幅图像
print(digits.images[0])
# 第一幅图像代表的数字含义
print(digits.target[0])
# 将第一幅图像显示出来
"""
plt.gray()
plt.imshow(digits.image[0])
plt.show()

"""
# 分割数据
train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.25, train_size=0.75)
print(train_x.max())
print((train_x > 1).sum())
print(train_x.shape[0]*train_x.shape[1])

# 采用Z-Score标准化
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)

# 创建LR分类器
lr = LogisticRegression(solver='liblinear', multi_class='auto')#数据集比较小，使用liblinear，数据集大使用sag
lr.fit(train_ss_x, train_y)
predict_y = lr.predict(test_ss_x)
print("LR的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))

# 创建线性 CART决策树分类器
model = DecisionTreeClassifier()
model.fit(train_ss_x, train_y)
predict_y = model.predict(test_ss_x)
print("CART的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))

# 创建LDA分类器
model = LinearDiscriminantAnalysis(n_components=2)
model.fit(train_ss_x, train_y)
predict_y = model.predict(test_ss_x)
print("LDA的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))

# 创建贝叶斯分类器
model = GaussianNB()
model.fit(train_ss_x, train_y)
predict_y = model.predict(test_ss_x)
print("朴素贝叶斯的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))

# 创建KNN分类器
model = KNeighborsClassifier()
model.fit(train_ss_x, train_y)
predict_y = model.predict(test_ss_x)
print("KNN的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))

# 创建AdaBoost分类器
# 弱分类器
dt_stump = DecisionTreeClassifier(max_depth=5, min_samples_leaf=1)
dt_stump.fit(train_ss_x, train_y)
#dt_stump_err = 1.0 - dt_stump.score(test_x, test_y)
# 设置AdaBoost迭代次数
n_estimators = 500
model = AdaBoostClassifier(base_estimator=dt_stump, n_estimators=n_estimators)
model.fit(train_ss_x, train_y)
predict_y = model.predict(test_ss_x)
print("AdaBoots的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))

# 创建XGBoost分类器
model = XGBClassifier()
model.fit(train_ss_x, train_y)
predict_y = model.predict(test_ss_x)
print("XGBoots的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))
