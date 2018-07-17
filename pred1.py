import pandas as pd
import numpy as np
import patsy
import statsmodels.api as sm
from sklearn import cross_validation
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC

class pred1:
    def __init__(self):
        df = pd.read_csv('./clean.csv')
        df.loc[:, 'cs_rent'] = df['cs_rent'].astype(int)

        f = 'cs_rent ~ cs_dist '
        y, X = patsy.dmatrices(f, df, return_type='dataframe')
        self.results = sm.OLS(y, X).fit()

#预测数据
    def predict1(self,dist):
        a1 = np.mat([1, dist])
        return self.results.predict(a1)[0]


P1 = pred1()




