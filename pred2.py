import pandas as pd
import numpy as np
import patsy
import statsmodels.api as sm


class pred2:
    def __init__(self):
        df = pd.read_csv('./clean.csv')
        f = 'cs_rent ~ cs_size '
        y, X = patsy.dmatrices(f, df, return_type='dataframe')
        self.results = sm.OLS(y, X).fit()
#预测数据
    def predict2(self,size):
        a1 = np.mat([1, size])
        return self.results.predict(a1)[0]


P2=pred2()

