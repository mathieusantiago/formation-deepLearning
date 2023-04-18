# Importer la bibliothèque pandas
import pandas as pd

# Lire le fichier CSV et le stocker dans un DataFrame
df = pd.read_csv('../DATA/Universities.csv')

# Afficher les 5 premières lignes du DataFrame
print(df.head())

# Regrouper les données par année, calculer la somme et trier par ordre décroissant
grouped_by_year = df.groupby('Year').sum().sort_index(ascending=False)

# Afficher le résultat du regroupement par année
print(grouped_by_year)

# Regrouper les données par année et secteur, puis calculer la somme
grouped_by_year_sector = df.groupby(['Year', 'Sector']).sum()

# Afficher le résultat du regroupement par année et secteur
print(grouped_by_year_sector)

# Regrouper les données par année et afficher des statistiques descriptives
stats_by_year = df.groupby('Year').describe().transpose()

# Afficher les statistiques descriptives par année
print(stats_by_year)