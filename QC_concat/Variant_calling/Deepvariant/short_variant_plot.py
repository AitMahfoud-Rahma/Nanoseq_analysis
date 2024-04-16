import matplotlib.pyplot as plt

input_file = "short_v_stat_concat.txt"
samples = []
nb_total_variants = []
nb_pass_variants = []

with open(input_file, 'r') as file:
    next(file)  
    for line in file:
        sample, total, pass_variants = line.strip().split('\t')
        samples.append(sample)
        nb_total_variants.append(int(total))
        nb_pass_variants.append(int(pass_variants))


plt.figure(figsize=(10, 6))

# Tracer le nombre de PASS variants
plt.bar(samples, nb_pass_variants, color='skyblue', label='PASS Variants')

# Tracer le nombre total de variants (en tant que ligne)
plt.plot(samples, nb_total_variants, color='orange', marker='o', linestyle='dashed', linewidth=2, markersize=8, label='Total Variants')

# Ajouter les étiquettes et la légende
plt.xlabel('Sample')
plt.ylabel('Number of Variants')
plt.title('Number of Short Variants identified by deepvariant')
plt.legend()

# Afficher le graphique
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("short_variant.png")
