import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm

input_file = "structural_v_stat_concat.txt"
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

#  PASS variants
plt.bar(samples, nb_pass_variants, color='skyblue', label='PASS Variants')

# total variants (as line)
plt.plot(samples, nb_total_variants, color='orange', marker='o', linestyle='dashed', linewidth=2, markersize=8, label='Total Variants')
plt.xlabel('Sample')
plt.ylabel('Number of Variants')
plt.title('Number of Structural Variants identified by CuteSV')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Nb_Structural_variant.png")
