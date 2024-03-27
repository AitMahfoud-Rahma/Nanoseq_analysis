import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm

output_file = "short_variants_stat.txt"

# Lecture du fichier de données
samples = []
num_variants_total = []
num_variants_pass = []

with open(output_file, 'r') as file:
    next(file)  # Ignorer la première ligne contenant les en-têtes
    for line in file:
        sample, total, pass_variants = line.strip().split('\t')
        samples.append(sample)
        num_variants_total.append(int(total))
        num_variants_pass.append(int(pass_variants))

# Création du graphique
plt.figure(figsize=(10, 6))

# Création de l'indice pour les échantillons
x = range(len(samples))

# Largeur des barres
bar_width = 0.35

# Tracer les barres pour le nombre total de variants
plt.bar(x, num_variants_total, bar_width, label='Total Variants')

# Tracer les barres pour le nombre de variants PASS, en les superposant
plt.bar([i + bar_width for i in x], num_variants_pass, bar_width, label='Variants PASS')

# Ajout de titres et de labels
plt.title('Number of variants per sample')
plt.xlabel('Samples')
plt.ylabel('Number of variants')

# Rotation des étiquettes de l'axe x pour une meilleure lisibilité
plt.xticks([i + bar_width / 2 for i in x], samples, rotation=45, ha='right')

# Affichage de la légende
plt.legend()

# Affichage du graphique
plt.tight_layout()  # Pour éviter que les étiquettes ne se chevauchent
plt.savefig("short_v_stat.png")
