
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


diamonds = pd.read_csv('../DATA/diamonds.csv')


diamonds.head()


diamonds.info()

# ## Tâches à effectuer


# ### Créer un diagramme de dispersion de la colonne prix par rapport à la colonne carat comme indiqué ci-dessous


sns.scatterplot(x='carat',y='price',data=diamonds);





# ### Utiliser le paramètre alpha et le paramètre edgecolor pour traiter le problème de chevauchement et le problème de marqueur de bord blanc.


sns.scatterplot(x='carat',y='price',data=diamonds,alpha=0.1,edgecolor=None);





# ### Agrandir le graphique précédent


plt.figure(figsize=(12,8))
sns.scatterplot(x='carat',y='price',data=diamonds,alpha=0.1,edgecolor=None);





# ### Créer un histogramme de la colonne des prix comme indiqué ci-dessous


plt.figure(figsize=(12,8))
sns.displot(diamonds['price'],kde=False)
plt.xlim(0,18000);





# ### Créer un graphique de comptage des instances par type de coupe comme indiqué ci-dessous


sns.countplot(x='cut',data=diamonds);





# ### Créer un grand diagramme en boîtes montrant la répartition des prix par type de coupe, comme indiqué ci-dessous


plt.figure(figsize=(12,8))
sns.boxplot(x='cut',y='price',data=diamonds);





# ### Défi ! Voyez si vous pouvez modifier l'ordre des boîtes à moustaches comme indiqué ci-dessous. N'hésitez pas à changer également la coloration, pour refléter cette relation entre les types de coupe.


diamonds['cut'].unique()
cut_order = ['Fair','Ideal','Good', 'Very Good','Premium']
plt.figure(figsize=(12,8))
sns.boxplot(x='cut',y='price',data=diamonds,order=cut_order,palette='cool');








