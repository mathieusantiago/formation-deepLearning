# Importer les bibliothèques numpy et pandas
import numpy as np
import pandas as pd

# Lire le fichier CSV et le stocker dans un DataFrame
df = pd.read_csv('../DATA/example.csv')

# Afficher le contenu du DataFrame
print(df)

# Enregistrer le DataFrame dans un nouveau fichier CSV sans inclure l'index
df.to_csv('../OUTPUT/output.csv', index=False)

# Afficher à nouveau le contenu du DataFrame
print(df)