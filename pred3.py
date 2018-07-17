from sklearn import cross_validation
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import pandas as pd

class pred3:
    def __init__(self):
        df = pd.read_csv('./clean.csv')
        df.loc[:, 'cs_rent'] = df['cs_rent'].astype(int)
        self.clf = OneVsRestClassifier(SVC(kernel='linear'))
        x = df.ix[:,:2]
        y = df.ix[:, 2]
        x_train, x_test, y_train, y_test = cross_validation.train_test_split(x.values, y.values, test_size=0.1)
        self.clf.fit(x_train, y_train)
#预测数据
    def predict3(self,size,type):
        x_test = [[size,type]]
        return self.clf.predict(x_test)[0]


P3 = pred3()
