import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Importer le jeu de données
path = 'DATA/fake_reg.csv'
abs_path = os.path.abspath(path)
df = pd.read_csv(abs_path)