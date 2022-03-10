"""
groupby is fast!

python pandas_ex/grouping.py
"""

import time
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

s = time.time()
iris.groupby('species').transform(lambda x: (x - x.mean()) / x.std())
e = time.time()
print("Groupby: {}".format(e - s))
