stateDev = False

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
from tensorflow.keras.callbacks import Callback

class TqdmProgressCallback(Callback):
    def __init__(self, total_epochs):
        self.total_epochs = total_epochs
        self.progress_bar = None

    def on_train_begin(self, logs=None):
        self.progress_bar = tqdm(total=self.total_epochs, desc="Training progress", ncols=100)

    def on_epoch_end(self, epoch, logs=None):
        self.progress_bar.update(1)

    def on_train_end(self, logs=None):
        self.progress_bar.close()


def devState():
    if stateDev:
        return plt.show()
    else:
        return print('  devState not display graph ')
    

def messagePrint(message):
        print ('\n' * 0)
        print(message)
        print ('\n'* 0)
        


# Importer le jeu de données
path = 'DATA/fake_reg.csv'
abs_path = os.path.abspath(path)
df = pd.read_csv(abs_path)

messagePrint('# START !!!')

# Afficher le jeu de données
messagePrint('# Afficher le jeu de données')
print(df.head())

# Afficher le graphique du jeu de données
sns.pairplot(df)
messagePrint('# Afficher le graphique du jeu de données')
devState()

# Importer train_test_split de sklearn
from sklearn.model_selection import train_test_split

# Définir les variables d'entrée et la variable cible
X = df[['feature1', 'feature2']].values
y = df['price'].values

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Afficher les dimensions des ensembles d'entraînement et de test
messagePrint('# Afficher les dimensions des ensembles d\'entraînement et de test')
print(X_train.shape)
print(X_test.shape)

from sklearn.preprocessing import MinMaxScaler

# Instancier le MinMaxScaler
scaler = MinMaxScaler()

# Adapter le scaler sur l'ensemble d'entraînement
scaler.fit(X_train)

# Transformer les ensembles d'entraînement et de test
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Créer un modèle séquentiel
model = Sequential()

# Ajouter des couches au modèle
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1))

# Compiler le modèle avec l'optimiseur et la fonction de perte
model.compile(optimizer='rmsprop', loss='mse')

# Entraîner le modèle sur l'ensemble d'entraînement
messagePrint('# démarage de l\'apprentisage')
model.fit(X_train, y_train, epochs=250, verbose=0, callbacks=[TqdmProgressCallback(total_epochs=250)])

# Obtenir l'historique des pertes
loss = model.history.history['loss']

# Tracer la perte d'entraînement par époque
sns.lineplot(x=range(len(loss)), y=loss)
plt.title("Perte sur le set d'entraînement par Epoch");
messagePrint('# Perte sur le set d\'entraînement par Epoch')
devState()

# Évaluer le modèle sur les ensembles d'entraînement et de test
training_score = model.evaluate(X_train, y_train, verbose=0)
test_score = model.evaluate(X_test, y_test, verbose=0)

# Afficher les scores
messagePrint('# Afficher les scores')

print(training_score)
print(test_score)

# Obtenir les prédictions du modèle sur l'ensemble de test
test_predictions = model.predict(X_test)

# Créer un DataFrame avec les vraies valeurs
pred_df = pd.DataFrame(y_test, columns=['Test Y'])

# Redimensionner les prédictions et les convertir en une série pandas
test_predictions = pd.Series(test_predictions.reshape(300,))

# Concaténer les vraies valeurs et les prédictions
pred_df = pd.concat([pred_df, test_predictions], axis=1)

# Renommer les colonnes
pred_df.columns = ['TestY', 'ModelPred']

# Tracer un nuage de points des vraies valeurs par rapport aux prédictions
sns.scatterplot(x='TestY', y='ModelPred', data=pred_df)
messagePrint('# PREDICTION GRAPH')
devState()

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Calculer l'erreur moyenne absolue et l'erreur quadratique moyenne
mae = mean_absolute_error(pred_df['TestY'], pred_df['ModelPred'])
mse = mean_squared_error(pred_df['TestY'], pred_df['ModelPred'])

messagePrint('# l\'erreur moyenne absolue et l\'erreur quadratique moyenne')
print(mae)
print(mse)

# Faire une prédiction pour un nouveau point de données
new_gem = [[998, 1000]]
new_gem = scaler.transform(new_gem)

from tensorflow.keras.models import load_model

# Sauvegarder le modèle dans un fichier
model.save('../OUTPUT/my_gen_model.h5')

# Charger le modèle à partir du fichier
later_model = load_model('../OUTPUT/my_gen_model.h5')

# Faire une prédiction avec le modèle chargé
prediction = later_model.predict(new_gem)

messagePrint('# PREDICTION')
print(prediction)
messagePrint('# END !!!')