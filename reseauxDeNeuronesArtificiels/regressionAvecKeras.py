import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
stateDev = True

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

plt.figure(figsize=(10, 6))
sns.histplot(df['price'])
# devState()

sns.countplot(x=df['bedrooms'])
# devState()

plt.figure(figsize=(12, 8))
sns.scatterplot(x='price', y='sqft_living', data=df)
# devState()

plt.figure(figsize=(12, 8))
sns.boxplot(x='bedrooms', y='price', data=df)
# devState()

plt.figure(figsize=(12, 8))
sns.scatterplot(x='price', y='long', data=df)
# devState()

plt.figure(figsize=(12, 8))
sns.scatterplot(x='price', y='lat', data=df)
# devState()

plt.figure(figsize=(12, 8))
sns.scatterplot(x='long', y='lat', data=df, hue='price')
# devState()

print(df.sort_values('price', ascending=False).head(20))

non_top_1_perc = df.sort_values('price', ascending=False).iloc[216:]

plt.figure(figsize=(12, 8))
sns.scatterplot(x='long', y='lat', data=non_top_1_perc,
                hue='price', edgecolor=None, alpha=0.2, palette='RdYlGn')
# devState()

plt.figure(figsize=(12, 8))
sns.boxenplot(x='waterfront', y='price', data=df)
devState()
