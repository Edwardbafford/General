"""
Use the built in replace function

python pandas_ex/replacing.py
"""

import time
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
s = time.time()
iris['species'].loc[iris['species'] == 'virginica'] = 'virginia'
e = time.time()
print("Replacing with loc: {}".format(e - s))

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
s = time.time()
iris.replace({'species': {'virginica': 'virginia'}}, inplace=True)
e = time.time()
print("Replacing with replace: {}".format(e - s))
