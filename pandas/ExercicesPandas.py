# %% [markdown]
# #### Importer Pandas

# %%
import pandas as pd

# %% [markdown]
# #### Lire le fichier 'african_econ_crises.csv'
# Il se trouve sous le dossier 01-Pandas ou DATA. Faites bien attention à l'endroit où se trouve le fichier .csv ! Si vous n'arrivez pas à le trouver ou à le lire, exécuter le notebook Solutions.

# %%
df = pd.read_csv('../DATA/african_econ_crises.csv')

# %% [markdown]
# #### Afficher les 5 premières lignes de l'ensemble de données

# %%
df.head()

# %%
# Ne rien écrire ici

# %% [markdown]
# #### Combien de pays sont représentés dans cet ensemble de données ?

# %%
df['country'].nunique()

# %%


# %% [markdown]
# #### Quels sont les pays représentés dans cet ensemble de données ?

# %%
df['country'].unique()

# %%


# %% [markdown]
# #### Quel est le pays dont le taux d'inflation annuel (CPI) est le plus élevé ? Quel était le taux d'inflation ?

# %%
df.sort_values('inflation_annual_cpi',ascending=False).head(1)

# %%


# %% [markdown]
# #### En quelle année le Kenya a-t-il connu sa première crise systémique ?

# %%
df[(df['country']=='Kenya') & (df['systemic_crisis']==1)].sort_values('year')

# %%


# %% [markdown]
# #### Combien de crises systémiques annuelles ont eu lieu dans chaque pays ?

# %%
crisis = df[df['systemic_crisis']==1]
crisis.groupby('country').count()['systemic_crisis']

# %%


# %% [markdown]
# #### Pendant combien d'années le Zimbabwe a-t-il connu un défaut de paiement de sa dette extérieure souveraine ?

# %%
len(df[(df['country']=='Zimbabwe') & (df['sovereign_external_debt_default']==1)])

# %%


# %% [markdown]
# #### En quelle année l'Algérie a-t-elle eu son taux de change le plus élevé ?

# %%
df[df['country']=="Algeria"].sort_values('exch_usd',ascending=False).head(1)

# %%



