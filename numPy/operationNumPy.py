import numpy as np

# Crée un tableau numpy de taille 10 commençant à 0
arr = np.arange(0,10)
print("arr = ", arr)

# Ajoute 5 à chaque élément du tableau
print("arr + 5 = ", arr + 5)

# Soustrait 2 à chaque élément du tableau
print("arr - 2 = ", arr - 2)

# Ajoute chaque élément du tableau avec celui ayant le même index
print("arr + arr = ", arr + arr)

# Multiplie chaque élément du tableau avec celui ayant le même index
print("arr * arr = ", arr * arr)

# Soustrait chaque élément du tableau avec celui ayant le même index
print("arr - arr = ", arr - arr)

# Affiche le tableau
print("arr = ", arr)

# Divise chaque élément du tableau avec celui ayant le même index
print("arr / arr = ", arr / arr)

# Calcule la racine carrée de chaque élément du tableau
print("np.sqrt(arr) = ", np.sqrt(arr))

# Calcule le sinus de chaque élément du tableau
print("np.sin(arr) = ", np.sin(arr))

# Calcule le logarithme naturel de chaque élément du tableau
print("np.log(arr) = ", np.log(arr))

# Affiche le tableau
print("arr = ", arr)

# Calcule la somme de tous les éléments du tableau
print("arr.sum() = ", arr.sum())

# Calcule la moyenne de tous les éléments du tableau
print("arr.mean() = ", arr.mean())

# Retourne l'élément ayant la valeur maximale dans le tableau
print("arr.max() = ", arr.max())

# Retourne l'élément ayant la valeur minimale dans le tableau
print("arr.min() = ", arr.min())

# Calcule la variance des éléments du tableau
print("arr.var() = ", arr.var())

# Calcule l'écart-type des éléments du tableau
print("arr.std() = ", arr.std())

# Crée un tableau numpy de taille 5x5 contenant les entiers de 0 à 24
arr_2d = np.arange(0,25).reshape(5,5)

# Affiche la forme (taille) du tableau
print("arr_2d.shape = ", arr_2d.shape)

# Affiche le tableau
print("arr_2d = \n", arr_2d)

# Calcule la somme des éléments pour chaque colonne du tableau
print("arr_2d.sum(axis=0) = ", arr_2d.sum(axis=0))

# Calcule la somme des éléments pour chaque ligne du tableau
print("arr_2d.sum(axis=1) = ", arr_2d.sum(axis=1))