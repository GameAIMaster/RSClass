from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression#逻辑回归
from xgboost import XGBClassifier #XGBoost
from sklearn.metrics import accuracy_score, roc_auc_score, auc, roc_curve, recall_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools

# plot confusion matrix
def plot_confusion_matrix(cm:np.array, classes:str, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Input
    - cm : 计算出的混淆矩阵的值
    - classes : 混淆矩阵中每一行每一列对应的列
    - normalize : True:显示百分比, False:显示个数
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(cm)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

pd.set_option('display.max_rows', 10, 'display.max_columns', 10)
# 加载数据
data = pd.read_csv("train.csv", usecols=[
 'Attrition',
 'BusinessTravel', # (0,1,2)
 'DistanceFromHome',
 'Education',
 'JobRole',
 'MonthlyIncome',
 'OverTime',
 'PerformanceRating',
 'TotalWorkingYears',
 'YearsAtCompany'])
# test_data = pd.read_csv("test.csv")
# 准备数据：数据预处理
# data['Hours_Player'] = df['Hours'].astype('float32')
data['Attrition'] = data['Attrition'].map({'Yes': 1, 'No': 0})
data['OverTime'] = data['OverTime'].map({'Yes': 1, 'No': 0})
data['BusinessTravel'] = data['BusinessTravel'].map({'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 2})
data = data.join(pd.get_dummies(data['JobRole'], prefix='JobRole'))
# print(data.head())
data_y = data['Attrition'].copy()
data.drop(columns=['Attrition', 'JobRole'], inplace=True)

# print(data.head())

train_x, test_x, train_y, test_y = train_test_split(data, data_y, test_size=0.4, train_size=0.6, random_state=172)
# 采用Z-Score标准化
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)
# 选择模型贝叶斯概率模型/LR分类器模型+深度学习
# 分割数据，将25%的数据作为测试集，其余的作为训练集
lr = LogisticRegression(solver='liblinear', multi_class='auto')#数据集比较小，使用liblinear，数据集大使用sag
lr.fit(train_ss_x, train_y)
predict_y = lr.predict(test_ss_x)
print("LR的准确率为：%0.4lf" % accuracy_score(predict_y, test_y))
print("LR的ROC AUC准确率为：%0.4lf" % roc_auc_score(test_y, lr.predict_proba(test_ss_x)[:, 1], average='macro'))
plot_confusion_matrix(confusion_matrix(test_y, predict_y), classes=['No', 'Yes'])
# 创建XGBoost分类器
# model = XGBClassifier(n_estimators=1200, max_depth=9, seed=2020)
# model.fit(train_ss_x, train_y, eval_metric='auc', verbose=False, eval_set=[(test_ss_x, test_y)])
# predict_y = model.predict(test_ss_x)
# print("XGBoots的ROC AUC准确率为：%0.4lf" % roc_auc_score(test_y, model.predict_proba(test_ss_x)[:, 1], average='macro'))
# plot_confusion_matrix(confusion_matrix(test_y, predict_y), classes=['No', 'Yes'])

# 训练模型

# 评估

# 超参数调整

# 预测
