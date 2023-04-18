# 1. Importer NumPy
import numpy as np

# 2. Créer un tableau de 10 zéros
np.zeros(10)

# 3. Créer un tableau contenant 10 uns
np.ones(10)

# 5. Créer un tableau d'entiers de 10 à 50
np.ones(10) * 5

# 5. Créer un tableau d'entiers de 10 à 50
np.arange(10, 51)

# 6. Créer un tableau de tous les entiers pairs de 10 à 50
np.arange(10, 51, 2)

# 7. Créer une matrice 3x3 avec des valeurs allant de 0 à 8
np.arange(4, 8)

# 8. Créer une matrice identité 3x3
np.arange(9).reshape(3,3)

# 9. Utiliser NumPy pour générer un nombre aléatoire entre 0 et 1
# NOTE : La valeur de votre résultat doit être différente de celle indiquée ci-dessous.
np.random.rand(1)

# 10. Utiliser NumPy pour générer un tableau de 25 nombres aléatoires échantillonnés à partir d'une distribution normale standard
# NOTE : Les valeurs de votre résultat doivent être différentes de celles indiquées ci-dessous.
np.random.randn(25)

# 11. Créer la matrice suivante :
arr = np.arange(1, 101) / 100
arr.reshape(10,10)

# 12. Créer un tableau de 20 points espacés linéairement entre 0 et 1 :
np.linspace(0, 1 , 20)

# Indexation et sélection NumPy
# Pour une matrice donnée de départ (n'oubliez pas de lancer la cellule ci-dessous !),vous aurez à reproduire les résultats de la matrice résultante

mat =np.arange(1 ,26).reshape(5,5)
mat[2:,1:]

# 13. Écrivez un code qui reproduit la sortie indiquée ci-dessous.# Attention de ne pas exécuter la cellule immédiatement au-dessus de la sortie, sinon vous ne pourrez plus voir celle-ci.
mat[3,4]

# 14. Ecrivez un code qui reproduit le résultat indiqué ci-dessous.
mat[:3, 1:2]

# 15. Ecrivez un code qui reproduit le résultat indiqué ci-dessous.
mat[4,:]

# 16. Ecrivez un code qui reproduit le résultat indiqué ci-dessous.
mat[3:5, :]

# 17. Ecrivez un code qui reproduit le résultat indiqué ci-dessous.
mat[3:5]

# 18. Obtenir la somme de toutes les valeurs de la matrice mat
mat.sum()

# 19. Obtenir l'écart type des valeurs de la matrice mat
mat.std()

# 20. Obtenir la somme de toutes les colonnes de la matrice mat
mat.sum(axis=0)

# Question bonus
# Nous avons beaucoup travaillé avec des données aléatoires avec NumPy, mais y a-t-il un moyen de s'assurer que nous obtenions toujours les mêmes nombres aléatoires ? Que signifie la valeur de seed ? Le nombre choisi est-il important ?
np.random.seed(101)
np.random.rand(1)


