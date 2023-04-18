# Importer les bibliothèques pandas, matplotlib.pyplot et seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lire le fichier CSV 'heart.csv' et le stocker dans un DataFrame
df = pd.read_csv('../DATA/heart.csv')

# Tracer un histogramme de la colonne 'age' du DataFrame
sns.displot(df['age'])
plt.show()

# Afficher les 5 premières lignes du DataFrame
print(df.head())

# Tracer un graphique en barres pour la colonne 'sex' du DataFrame
sns.countplot(x='sex', data=df)
plt.show()

# Tracer un graphique en barres pour la colonne 'target' du DataFrame
sns.countplot(x='target', data=df)
plt.show()

# Tracer un graphique en barres pour la colonne 'cp' du DataFrame
sns.countplot(x='cp', data=df)
plt.show()

# Tracer un graphique en barres pour la colonne 'target' du DataFrame avec la colonne 'sex' comme hue
sns.countplot(x='target', data=df, hue='sex')
plt.show()

# Tracer un graphique en barres pour la colonne 'target' du DataFrame avec la colonne 'sex' comme hue et une palette 'prism'
sns.countplot(x='target', data=df, hue='sex', palette='prism')
plt.show()

# Tracer un boxplot pour les colonnes 'sex' et 'age' du DataFrame
sns.boxplot(x='sex', y='age', data=df)
plt.show()

# Tracer un boxplot pour les colonnes 'target' et 'age' du DataFrame
sns.boxplot(x='target', y='age', data=df)
plt.show()

# Tracer un boxplot pour les colonnes 'target' et 'thalach' du DataFrame avec la colonne 'sex' comme hue
sns.boxplot(x='target', y='thalach', data=df, hue='sex')
plt.show()

# Tracer un nuage de points pour les colonnes 'chol' et 'thalach' du DataFrame avec la colonne 'sex' comme hue et la colonne 'age' comme taille des points
sns.scatterplot(x='chol', y='thalach', data=df, hue='sex', palette='prism', size='age')
plt.show()

# Lire le fichier CSV 'iris.csv' et le stocker dans un DataFrame
iris = pd.read_csv('../DATA/iris.csv')

# Afficher le DataFrame 'iris'
print(iris)

# Tracer un pairplot pour le DataFrame 'iris'
sns.pairplot(iris)
plt.show()

# Tracer un pairplot pour le DataFrame 'iris' avec la colonne 'species' comme hue
sns.pairplot(iris, hue='species')
plt.show()