
import numpy as np
import pandas  as pd


labales = ['a','b','c']

my_list = [10,20,30]

arr = np.array([10,20,30])

d = {'a': 10, 'b': 20, 'c': 30}


pd.Series(data=my_list)


pd.Series(my_list, labales)


pd.Series(arr, labales)


pd.Series(d)


sales_Q1 = pd.Series(data=[250,450,200,150],index=['USA','China', 'India', 'French'])


sales_Q1


sales_Q2 = pd.Series(data=[260,500,210,100],index=['USA','China', 'India', 'Japan'])


sales_Q2


sales_Q2['China']


sales_Q2[0]


sales_Q1 + sales_Q2


# Importer les bibliothèques numpy et pandas
import numpy as np
import pandas as pd

# Créer des étiquettes, une liste, un tableau numpy et un dictionnaire
labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}

# Créer une série pandas à partir de la liste 'my_list'
series_from_list = pd.Series(data=my_list)

# Afficher la série créée à partir de la liste
print(series_from_list)

# Créer une série pandas à partir de la liste 'my_list' avec les étiquettes 'labels'
series_from_list_labels = pd.Series(my_list, labels)

# Afficher la série créée à partir de la liste et des étiquettes
print(series_from_list_labels)

# Créer une série pandas à partir du tableau numpy 'arr' avec les étiquettes 'labels'
series_from_arr = pd.Series(arr, labels)

# Afficher la série créée à partir du tableau numpy et des étiquettes
print(series_from_arr)

# Créer une série pandas à partir du dictionnaire 'd'
series_from_dict = pd.Series(d)

# Afficher la série créée à partir du dictionnaire
print(series_from_dict)

# Créer une série pandas pour les ventes du premier trimestre
sales_Q1 = pd.Series(data=[250, 450, 200, 150], index=['USA', 'China', 'India', 'French'])

# Afficher les ventes du premier trimestre
print(sales_Q1)

# Créer une série pandas pour les ventes du deuxième trimestre
sales_Q2 = pd.Series(data=[260, 500, 210, 100], index=['USA', 'China', 'India', 'Japan'])

# Afficher les ventes du deuxième trimestre
print(sales_Q2)

# Accéder à la valeur de la série 'sales_Q2' pour la Chine
print(sales_Q2['China'])

# Accéder à la première valeur de la série 'sales_Q2'
print(sales_Q2[0])

# Additionner les séries 'sales_Q1' et 'sales_Q2'
total_sales = sales_Q1 + sales_Q2

# Afficher les ventes totales
print(total_sales)