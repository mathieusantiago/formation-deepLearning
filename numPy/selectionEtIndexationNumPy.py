import numpy as np

# Créer un tableau allant de 0 à 10 avec un pas par défaut de 1
arr = np.arange(0, 11)

# Récupérer la valeur à l'index 8
print(arr[8])

# Récupérer un tableau allant de l'index 1 à 4 (5 n'est pas inclus)
print(arr[1:5])

# Récupérer un tableau allant de l'index 0 à 4 (5 n'est pas inclus)
print(arr[:5])

# Récupérer un tableau allant de l'index 5 jusqu'à la fin
print(arr[5:])

# Diffuser (broadcast) la valeur 100 dans le tableau de l'index 0 à 4
arr[0:5] = 100
print(arr)

# Réinitialiser le tableau à sa forme originale
arr = np.arange(0, 11)

# Créer une tranche (slice) du tableau allant de l'index 0 à 4
slice_of_arr = arr[0:5]
print(slice_of_arr)

# Mettre à jour la tranche pour que toutes ses valeurs soient 99
slice_of_arr[:] = 99
print(slice_of_arr)

# Les modifications apportées à la tranche affectent le tableau d'origine
print(arr)

# Créer une copie du tableau pour éviter les modifications sur le tableau d'origine
arr_copy = arr.copy()

# Mettre à jour toutes les valeurs de la copie du tableau pour qu'elles soient toutes égales à 100
arr_copy[:] = 100
print(arr_copy)

# Le tableau d'origine reste inchangé
print(arr)

# Créer un tableau 2D
arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)

# Récupérer le nombre de lignes et de colonnes dans le tableau
print(arr_2d.shape)

# Récupérer la valeur à l'index (1,1)
print(arr_2d[1][1])
print(arr_2d[1, 1])

# Récupérer un sous-tableau allant de la ligne 0 à la ligne 1 (2 n'est pas inclus) et de la colonne 1 jusqu'à la fin
print(arr_2d[:2, 1:])

# Créer un tableau allant de 1 à 10
arr = np.arange(1,11)

# Vérifier pour chaque valeur du tableau si elle est supérieure à 4
print(arr > 4)

# Récupérer un tableau contenant uniquement les valeurs supérieures à 4 du tableau d'origine
bool_arr = arr > 4
print(arr[bool_arr])
print(arr[arr > 4])