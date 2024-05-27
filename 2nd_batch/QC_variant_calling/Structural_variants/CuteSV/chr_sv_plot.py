import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('chr_sv.csv')

# Filter to remove chromosomes 'chrUn'
df = df[~df['Chromosome'].str.contains('chrUn')]

# Liste of chromosomes for dogs (X et Y included)
chromosomes = [f'chr{i}' for i in range(1, 39)] + ['chrX', 'chrY']

# order chromosomes
df['Chromosome'] = pd.Categorical(df['Chromosome'], categories=chromosomes, ordered=True)
df = df.sort_values(['File', 'Chromosome'])

# Create a plot for each file and save it
files = df['File'].unique()

for file in files:
    subset = df[df['File'] == file]
    plt.figure(figsize=(12, 6))
    plt.bar(subset['Chromosome'].astype(str), subset['Variant Count'])  # to resolve error
    plt.xlabel('Chromosomes')
    plt.ylabel('Number of SVs')
    plt.title(f'Number of Structural Variants for {file}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f'{file}_variant_count.png')
    plt.close()