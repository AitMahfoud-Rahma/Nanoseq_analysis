import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm

input_file = "/groups/dog/stage/rahma/2nd_batch/results/variant_calling/sniffles_before_sort/nb_sv_sni.txt"
samples = []
nb_total_variants = []
nb_pass_variants = []
nb_non_pass_variants = []

with open(input_file, 'r') as file:
    next(file)  
    for line in file:
        sample, total, pass_variants = line.strip().split('\t')
        samples.append(sample)
        nb_total_variants.append(int(total))
        nb_pass_variants.append(int(pass_variants))
        nb_non_pass_variants.append(int(total) - int(pass_variants))  # Calcul des non PASS variants

plt.figure(figsize=(10, 6))

# PASS variants
plt.bar(samples, nb_pass_variants, color='skyblue', label='PASS Variants')

# Non PASS variants
plt.bar(samples, nb_non_pass_variants, bottom=nb_pass_variants, color='orange', label='Non PASS Variants')

plt.xlabel('Samples')
plt.ylabel('Number of Variants')
plt.title('Number of Structural Variants identified by Sniffles')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/Nb_SV_sniffles2.png")
