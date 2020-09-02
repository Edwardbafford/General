"""
pandas loc and iloc are fast...

python pandas_ex/indexing.py
"""

import time
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

s = time.time()
iris.iloc[10:75]
e = time.time()
print("Rows with iloc: {}".format(e - s))

s = time.time()
iris.loc[range(5, 70)]
e = time.time()
print("Rows with loc: {}".format(e - s))

s = time.time()
iris.iloc[:, :3]
e = time.time()
print("Columns with iloc: {}".format(e - s))

s = time.time()
iris.loc[:, ['sepal_width', 'petal_length', 'petal_width']]
e = time.time()
print("Columns with loc: {}".format(e - s))
