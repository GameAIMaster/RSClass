from tpot import TPOTClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np

# 加载数据
digits = load_digits()
data = digits.data
train_x, test_x, train_y, test_y = train_test_split(digits.data.astype(np.float64),
                                                    digits.target.astype(np.float64), train_size=0.75, test_size=0.25)

tpot = TPOTClassifier(generations=5, population_size=20, verbosity=2)
tpot.fit(train_x, train_y)
print(tpot.score(test_x,test_y))
tpot.export('tpot_mnist_pipeline.py')