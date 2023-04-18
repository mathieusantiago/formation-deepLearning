import numpy as np

# Créer une liste Python
my_list = [1, 2, 3]

# Créer un tableau numpy à partir de la liste Python car les tableaux numpy sont plus efficaces
my_array = np.array(my_list)
print(my_array)

# Créer une liste imbriquée (nested)
nested_list = [[1, 2], [3, 4], [5, 6]]

# Il est possible de travailler avec une liste imbriquée
nested_array = np.array(nested_list)
print(nested_array)

# Créer un tableau d'entiers (début, fin, pas)
np_array_range = np.arange(0, 10)
print(np_array_range)

# Créer un tableau de 0 de dimension 4x10, si dtype n'est pas spécifié, c'est un float
zeros_array = np.zeros((4, 10))
print(zeros_array)

# Créer un tableau de 1 de dimension 4x10, si dtype n'est pas spécifié, c'est un float
ones_array = np.ones((4, 10))
print(ones_array)

# Créer un tableau linéairement espacé entre 0 et 10 avec 21 éléments
linspace_array = np.linspace(0, 10, 21)
print(linspace_array)

# Créer une matrice identité de dimension 5x5
identity_matrix = np.eye(5)
print(identity_matrix)

# Générer un nombre aléatoire uniforme entre 0 et 1
rand_num = np.random.rand(2)
print(rand_num)

# Générer une matrice aléatoire uniforme de dimension 3x4
rand_matrix = np.random.rand(3, 4)
print(rand_matrix)

# Générer une matrice aléatoire normalement distribuée de dimension 5x5
randn_matrix = np.random.randn(5, 5)
print(randn_matrix)

# Générer un tableau d'entiers aléatoires entre 1 et 100 de taille 2x3
randint_array = np.random.randint(1, 100, (2, 3))
print(randint_array)

# Définir une graine (seed) pour les nombres aléatoires afin d'avoir des résultats reproductibles
np.random.seed(42)
seeded_rand = np.random.rand(4)
print(seeded_rand)

# Créer un tableau numpy avec des nombres aléatoires
arr = np.arange(25)
print(arr)

# Créer un tableau numpy avec des nombres aléatoires entiers entre 0 et 50 de taille 10
ranarr = np.random.randint(0, 50, 10)
print(ranarr)

# Obtenir la forme du tableau 'arr'
print(arr.shape)

# Redimensionner le tableau 'arr' en une matrice 5x5
arr = arr.reshape(5, 5)
print(arr)

# Obtenir la valeur maximale du tableau 'ranarr'
print(ranarr.max())

# Obtenir l'indice de la valeur maximale du tableau 'ranarr'
print(ranarr.argmax())

# Obtenir la valeur minimale du tableau 'ranarr'
print(ranarr.min())

# Obtenir l'indice de la valeur minimale du tableau 'ranarr'
print(ranarr.argmin())

# Obtenir le type de données
print(ranarr.dtype)

# Créer un nouveau tableau numpy avec des nombres aléatoires
myarr = np.random.rand(4)
print(myarr)

# Obtenir le type de données du tableau 'myarr'
print(myarr.dtype)