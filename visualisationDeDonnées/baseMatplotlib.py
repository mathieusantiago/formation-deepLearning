# Importer les bibliothèques numpy, pandas et matplotlib.pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Créer des listes x et y pour les données à tracer
x = [0, 1, 2]
y = [100, 200, 300]

# Tracer les données x et y avec une ligne
plt.plot(x, y)

# Afficher le graphique
plt.show()

# Créer un DataFrame pour les données de logement
housing = pd.DataFrame({'rooms': [1, 1, 2, 2, 2, 3, 3, 3],
                        'price': [100, 120, 190, 200, 230, 310, 330, 305]})

# Afficher le DataFrame 'housing'
print(housing)

# Tracer un nuage de points pour les données de logement
plt.scatter(housing['rooms'], housing['price'])

# Afficher le nuage de points
plt.show()

# Tracer les données x et y avec des options de style spécifiques
plt.plot(x, y, color='red', marker='o', markersize=15, linestyle='--')

# Définir les limites des axes x et y
plt.xlim(0, 2)
plt.ylim(0, 300)

# Ajouter un titre et des étiquettes pour les axes x et y
plt.title('titre')
plt.xlabel('Label x')
plt.ylabel('Label y')

# Afficher le graphique avec les options de style spécifiques
plt.show()