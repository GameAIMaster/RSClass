from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits

# 加载数据
digits = load_digits()
data = digits.data
# 准备数据：数据预处理
# 分割数据，将25%的数据作为测试集，其余的作为训练集
train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.25, random_state=33)
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)
# 选择模型CART 创建CART分类器
cart = DecisionTreeClassifier(min_samples_leaf=1, min_samples_split=3)
# 训练模型
dt_cart = cart.fit(train_ss_x, train_y)
# 评估
predict_y = dt_cart.predict(test_ss_x)
# 超参数调整

# 预测
print('CART准确率：%0.4lf' % accuracy_score(predict_y, test_y))