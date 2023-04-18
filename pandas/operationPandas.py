# Importer la bibliothèque pandas
import pandas as pd

# Créer un DataFrame avec des données spécifiques
df_one = pd.DataFrame({'k1': ['A', 'A', 'B', 'B', 'C', 'C'],
                       'col1': [100, 200, 300, 300, 400, 500],
                       'col2': ['NY', 'CA', 'WA', 'WA', 'AK', 'NV']})

# Afficher le DataFrame créé
print(df_one)

# Afficher les valeurs uniques de la colonne 'col2'
print(df_one['col2'].unique())

# Afficher les valeurs uniques de la colonne 'k1'
print(df_one['k1'].unique())

# Afficher le décompte des valeurs de la colonne 'col2'
print(df_one['col2'].value_counts())

# Supprimer les lignes en double du DataFrame
unique_df_one = df_one.drop_duplicates()

# Afficher le DataFrame sans les lignes en double
print(unique_df_one)

# Ajouter une nouvelle colonne 'new' en multipliant la colonne 'col1' par 10
df_one['new'] = df_one['col1'] * 10

# Afficher le DataFrame avec la nouvelle colonne 'new'
print(df_one)

# Définir une fonction pour récupérer la première lettre d'une chaîne de caractères
def grab_first_letter(state):
    return state[0]

# Appliquer la fonction 'grab_first_letter' sur la colonne 'col2'
first_letters = df_one['col2'].apply(grab_first_letter)

# Afficher les premières lettres obtenues
print(first_letters)

# Ajouter une nouvelle colonne 'first_letter' avec les premières lettres de la colonne 'col2'
df_one['first_letter'] = df_one['col2'].apply(grab_first_letter)

# Afficher le DataFrame avec la nouvelle colonne 'first_letter'
print(df_one)

# Définir une fonction pour vérifier si la première lettre d'une chaîne de caractères est 'W'
def complex_letter(state):
    if state[0] == 'W':
        return 'Washington'
    else:
        return 'Error'

# Appliquer la fonction 'complex_letter' sur la colonne 'col2'
complex_results = df_one['col2'].apply(complex_letter)

# Afficher les résultats obtenus
print(complex_results)

# Afficher la colonne 'k1'
print(df_one['k1'])

# Créer un dictionnaire pour mapper les valeurs de la colonne 'k1'
my_map = {'A': 1, 'B': 2, 'C': 3}

# Appliquer la correspondance sur la colonne 'k1'
mapped_values = df_one['k1'].map(my_map)

# Afficher les valeurs mappées
print(mapped_values)

# Ajouter une nouvelle colonne 'num' avec les valeurs mappées de la colonne 'k1'
df_one['num'] = df_one['k1'].map(my_map)

# Afficher le DataFrame avec la nouvelle colonne 'num'
print(df_one)

# Trouver la valeur maximale de la colonne 'col1'
print(df_one['col1'].max())

# Trouver l'index de la valeur maximale de la colonne 'col1'
print(df_one['col1'].idxmax())

# Trouver l'index de la valeur minimale de la colonne 'col1'
print(df_one['col1'].idxmin())

# Afficher les noms de colonnes du DataFrame
print(df_one.columns)

# Renommer les colonnes du DataFrame
df_one.columns = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']

# Afficher le DataFrame avec les nouvelles étiquettes de colonnes
print(df_one)

# Trier le DataFrame en fonction de la colonne 'c3'
sorted_df_one = df_one.sort_values('c3')

# Afficher le DataFrame trié
print(sorted_df_one)

# Trier le DataFrame en fonction de la colonne 'c3' dans l'ordre décroissant
sorted_descending_df_one = df_one.sort_values('c3', ascending=False)

# Afficher le DataFrame trié dans l'ordre décroissant
print(sorted_descending_df_one)

# Créer un DataFrame 'features'
features = pd.DataFrame({'A': [100, 200, 300, 400, 500],
'B': [12, 13, 14, 15, 16]})

# Créer un DataFrame 'predictions'
predictions = pd.DataFrame({'pred': [0, 1, 1, 0, 1]})

# Afficher le DataFrame 'features'
print(features)

# Afficher le DataFrame 'predictions'
print(predictions)

# Concaténer les DataFrames 'features' et 'predictions' en ajoutant les colonnes
concatenated_df = pd.concat([features, predictions], axis=1)

# Afficher le DataFrame concaténé
print(concatenated_df)

# Afficher la colonne 'c1' du DataFrame 'df_one'
print(df_one['c1'])

# Convertir la colonne 'c1' en variables indicatrices (dummy variables)
dummy_c1 = pd.get_dummies(df_one['c1'])

# Afficher les variables indicatrices de la colonne 'c1'
print(dummy_c1)