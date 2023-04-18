import numpy as np
import pandas  as pd

columns = ['W','X','Y','Z']

index = ['A','B','C','D', 'E']

from numpy.random import randint

np.random.seed(42)
data = randint(-100 , 100 , (5,4))

print(data)

df = pd.DataFrame(data, index , columns)

print(df)

df['W']

df[['W','Z']]

df["new"] = df['W'] + df['Y']

print(df)

df = df.drop('new', axis=1)

print(df)

df.loc[['A', 'E']]

df.iloc[[0, 2]]

df.iloc[0:3]

df.drop('C')

df.loc['A', 'W']

df.loc[['A','C'], 'W']

df.loc[['A','C'],['W', 'Y']]

print(df)

df[df > 0]

print(df)

df[df['X'] > 0]

df[df['X'] > 0]['W']

df[df['X'] > 0].iloc[0]

df[(df['W'] > 0) & (df['Y'] > 1)]

print(df)

df.reset_index()

new_ind = ['CA', 'NY', 'WY', 'OR', 'CO']

df['States'] = new_ind

print(df)

df = df.set_index('States')

print(df)

df.columns

df.describe()

df.info()

df.dtypes