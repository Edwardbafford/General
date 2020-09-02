"""
* range
* iterrows
* apply

python pandas_ex/looping.py
"""

import time
import numpy as np
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

s = time.time()
for index in range(iris.shape[0]):
    value = iris.iloc[index]
    np.sqrt(value['sepal_width'])
e = time.time()
print("Looping with range: {}".format(e - s))

s = time.time()
for index, value in iris.iterrows():
    np.sqrt(value['sepal_width'])
e = time.time()
print("Looping with iterrows: {}".format(e - s))

s = time.time()
iris['sepal_width'].apply(lambda x : np.sqrt(x))
e = time.time()
print("'Looping' with apply: {}".format(e - s))


