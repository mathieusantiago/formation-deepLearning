stateDev = True

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

path = 'DATA/kc_house_data.csv'
abs_path = os.path.abspath(path)
df = pd.read_csv(abs_path)

def devState():
    if stateDev:
        return plt.show()
    else:
        return print('  devState not display graph ')
    

print(df.isnull().sum())

df.describe().transpose

plt.figure(figsize=(10,6))
sns.distplot(df['price'])
devState()

sns.countplot(df['bedrooms'])
devState()

df.corr()