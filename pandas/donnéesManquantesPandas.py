# Importer les bibliothèques numpy et pandas
import numpy as np
import pandas as pd

# Créer un DataFrame avec des valeurs manquantes (np.nan)
df = pd.DataFrame({
                    'A': [1, 2, np.nan, 4],
                    'B': [5, np.nan, np.nan, 8],
                    'C': [10, 20, 30, 40]
                  })

# Remplacer les valeurs manquantes par la moyenne de chaque colonne
filled_df = df.fillna(df.mean())

# Afficher le DataFrame avec les valeurs manquantes remplacées
print(filled_df)

# Supprimer les colonnes ayant au moins 3 valeurs non manquantes
df_dropped = df.dropna(axis=1, thresh=3)

# Afficher le DataFrame après suppression des colonnes
print(df_dropped)

# Afficher les types de données de chaque colonne
print(df.dtypes)

# Remplacer les valeurs manquantes par la chaîne 'A VALUE'
filled_with_string = df.fillna(value='A VALUE')

# Afficher le DataFrame avec les valeurs manquantes remplacées par la chaîne 'A VALUE'
print(filled_with_string)

# Remplacer les valeurs manquantes de la colonne 'B' par la moyenne de cette colonne
filled_with_mean = df.fillna(value=df['B'].mean())

# Afficher le DataFrame avec les valeurs manquantes remplacées par la moyenne de la colonne 'B'
print(filled_with_mean)