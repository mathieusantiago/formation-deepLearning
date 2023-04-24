# Importer les bibliothèques nécessaires
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Variable permettant d'afficher ou non les graphiques
stateDev = True

# Chemin d'accès relatif au fichier de données
path = 'DATA/kc_house_data.csv'
# Chemin d'accès absolu au fichier de données
abs_path = os.path.abspath(path)
# Charger les données dans un DataFrame pandas
df = pd.read_csv(abs_path)

# Fonction permettant d'afficher les graphiques si stateDev est True
def devState():
    if stateDev:
        return plt.show()
    else:
        return print('  devState not display graph ')

# Affiche le nombre de valeurs manquantes par colonne
# print(df.isnull().sum())

# Affiche les statistiques descriptives du DataFrame
df.describe().transpose()

# Crée un histogramme de la colonne 'price'
# plt.figure(figsize=(12,8))
# sns.distplot(df['price']);

# Affiche le graphique si stateDev est True
# devState()

# Crée un graphique en barres du nombre de chambres
# sns.countplot(df['bedrooms']);

# Affiche le graphique si stateDev est True
# devState()

# Crée un nuage de points entre 'price' et 'sqft_living'
# plt.figure(figsize=(12, 8))
# sns.scatterplot(x='price', y='sqft_living', data=df)

# Affiche le graphique si stateDev est True
# devState()

# Crée un diagramme à moustaches entre 'bedrooms' et 'price'
# plt.figure(figsize=(12, 8))
# sns.boxplot(x='bedrooms', y='price', data=df)

# Affiche le graphique si stateDev est True
# devState()

# Crée un nuage de points entre 'price' et 'long' (longitude)
# plt.figure(figsize=(12, 8))
# sns.scatterplot(x='price', y='long', data=df)

# Affiche le graphique si stateDev est True
# devState()

# Crée un nuage de points entre 'price' et 'lat' (latitude)
# plt.figure(figsize=(12, 8))
# sns.scatterplot(x='price', y='lat', data=df)

# Affiche le graphique si stateDev est True
# devState()

# Crée un nuage de points entre 'long' (longitude) et 'lat' (latitude) avec une couleur basée sur 'price'
# plt.figure(figsize=(12, 8))
# sns.scatterplot(x='long', y='lat', data=df, hue='price')

# Affiche le graphique si stateDev est True
# devState()

# Affiche les 20 maisons les plus chères
# print(df.sort_values('price', ascending=False).head(20))

# Supprime les 1% de maisons les plus chères pour éviter les valeurs aberrantes
non_top_1_perc = df.sort_values('price', ascending=False).iloc[216:]

# Crée un nuage de points entre 'long' (longitude) et 'lat' (latitude) avec une couleur basée sur 'price', sans les valeurs aberrantes
# plt.figure(figsize=(12, 8))
# sns.scatterplot(x='long', y='lat', data=non_top_1_perc,
#                 hue='price', edgecolor=None, alpha=0.2, palette='RdYlGn')
# devState()
# Crée un diagramme en boîte (boxenplot) entre 'waterfront' et 'price'
# plt.figure(figsize=(12, 8))
# sns.boxenplot(x='waterfront', y='price', data=df)

# Supprime la colonne 'id' du DataFrame
df = df.drop('id',axis=1)

# Convertit la colonne 'date' en objet datetime
df['date'] = pd.to_datetime(df['date'])

# Ajoute une colonne 'year' en extrayant l'année de la colonne 'date'
df['year'] = df['date'].apply(lambda date: date.year)

# Ajoute une colonne 'month' en extrayant le mois de la colonne 'date'
df['month'] = df['date'].apply(lambda date: date.month)

# Crée un diagramme à moustaches entre 'month' et 'price'
# sns.boxplot(x='month', y='price', data=df)

# Affiche la moyenne des prix par mois
# plt.figure(figsize=(12,8))
# df.groupby('year').mean()['price'].plot();

# Supprime la colonne 'date' du DataFrame
df = df.drop('date',axis=1)

# Affiche le nombre d'occurrences pour chaque code postal
# print(df['zipcode'].value_counts())

# Supprime la colonne 'zipcode' du DataFrame
df = df.drop('zipcode',axis=1)

# Affiche le nombre d'occurrences pour chaque année de rénovation
# print(df['yr_renovated'].value_counts())

# Affiche le nombre d'occurrences pour chaque surface habitable du sous-sol
# print(df['sqft_basement'].value_counts())

# Sépare le DataFrame en variables indépendantes (X) et dépendante (y)
X = df.drop('price',axis=1)
y = df['price']

# Importer la fonction de séparation des données
from sklearn.model_selection import train_test_split

# Sépare les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Importer le module de normalisation MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

# Crée un objet MinMaxScaler
scaler = MinMaxScaler()

# Normalise les données d'entraînement avec le MinMaxScaler
X_train= scaler.fit_transform(X_train)

# Normalise les données de test avec le MinMaxScaler
X_test = scaler.transform(X_test)

# Importer les modules TensorFlow nécessaires
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam

# Crée un modèle de réseau de neurones séquentiel
model = Sequential()

# Ajoute des couches denses au modèle avec des fonctions d'activation ReLU
model.add(Dense(19,activation='relu'))
model.add(Dense(19,activation='relu'))
model.add(Dense(19,activation='relu'))
model.add(Dense(19,activation='relu'))

# Ajoute une couche de sortie avec une seule unité (pour la prédiction du prix)
model.add(Dense(1))

# Compile le modèle avec l'optimiseur Adam et la fonction de perte d'erreur quadratique moyenne (mse)
model.compile(optimizer='adam',loss='mse')
# Entraîne le modèle sur les données d'entraînement et évalue les performances sur les données de test
model.fit(x=X_train,y=y_train.values,
          validation_data=(X_test,y_test.values),
          batch_size=128,epochs=400)

# Crée un DataFrame avec l'historique des pertes pendant l'entraînement
losses = pd.DataFrame(model.history.history)

# Affiche un graphique de l'évolution des pertes d'entraînement et de validation
losses.plot()

# Importer les métriques d'évaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, explained_variance_score

# Effectuer des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# Afficher l'erreur absolue moyenne
# print(mean_absolute_error(y_test, predictions))

# Afficher la racine de l'erreur quadratique moyenne
# print(np.sqrt(mean_squared_error(y_test,predictions)))

# Afficher le score de variance expliquée
# print(explained_variance_score(y_test, predictions))

# Crée un nuage de points entre les valeurs réelles et les prédictions
plt.scatter(y_test,predictions)
# Ajoute une ligne diagonale rouge pour les prédictions parfaites
plt.plot(y_test,y_test,'r')

# Calcule les erreurs entre les valeurs réelles (y_test) et les prédictions du modèle
# en soustrayant les prédictions des valeurs réelles
errors = y_test.values.reshape(6480, 1) - predictions

# Affiche un histogramme pour visualiser la distribution des erreurs
# sns.histplot(errors)

# Sélectionne une maison pour effectuer une prédiction
single_house = df.drop('price', axis=1).iloc[0]

# Normalise les caractéristiques de la maison avec le MinMaxScaler
single_house = scaler.transform(single_house.values.reshape(-1, 19))

# Effectue une prédiction de prix pour la maison sélectionnée
print(model.predict(single_house))

# Affiche le graphique si stateDev est True
devState()