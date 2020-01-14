import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
digits = load_digits()
data = digits.data
# tpot_data = pd.read_csv('mnist.csv', sep='COLUMN_SEPARATOR', dtype=np.float64)
# features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
    train_test_split(digits.data.astype(np.float64),
                     digits.target.astype(np.float64), train_size=0.75, test_size=0.25)

# Average CV score on the training set was: 0.9866363761531047
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=GradientBoostingClassifier(learning_rate=0.001, max_depth=4, max_features=0.1, min_samples_leaf=1, min_samples_split=9, n_estimators=100, subsample=0.6000000000000001)),
    KNeighborsClassifier(n_neighbors=2, p=2, weights="distance")
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

print("TPOT的准确率为：%0.4lf" % accuracy_score(results, testing_target))
