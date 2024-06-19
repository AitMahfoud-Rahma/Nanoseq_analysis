import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('chr_svtypes_len.csv')

# Compter le nombre de variants par fichier et par chromosome
variant_counts = df.groupby(['File', 'Chromosome']).size().reset_index(name='Variant Count')

# Sauvegarder les résultats dans un nouveau fichier CSV
variant_counts.to_csv('chr_sv.csv', index=False)
