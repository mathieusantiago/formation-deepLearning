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


# print(df.isnull().sum())

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

df.drop('id', axis=1)

df['date'] = pd.to_datetime(df['date'])

df['year'] = df['date'].apply(lambda date: date.year)
df['month'] = df['date'].apply(lambda date: date.month)

sns.boxplot(x='month', y='price', data=df)

df.groupby('month').mean()['price'].plot()

df = df.drop('date', axis=1)

# print(df['zipcode'].value_counts())

df = df.drop('zipcode', axis=1)

# print(df['yr_renovated'].value_counts())

# print(df['sqlt_basement'].value_counts())

X = df.drop('price',axis=1)
y = df['price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))

model.add(Dense(1))

model.compile(optimizer='adam',loss='mse')

model.fit(x=X_train,y=y_train.values,
          validation_data=(X_test,y_test.values),
          batch_size=128,epochs=400)


# devState()
