import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm

output_file = "short_variants_stat.txt"
samples = []
num_variants = []

with open(output_file, 'r') as file:
    next(file) 
    for line in file:
        sample, variants = line.strip().split('\t')
        samples.append(sample)
        num_variants.append(int(variants))

sample_colors = {}
prefixes = set(sample.split('-')[0] for sample in samples) 
num_prefixes = len(prefixes)
colors = cm.tab10(range(num_prefixes)) 

for i, prefix in enumerate(sorted(prefixes)):
    for j in range(2): 
        sample = f"{prefix}-{j+1}"
        sample_colors[sample] = colors[i]

plt.figure(figsize=(10, 6))
for sample, variants in zip(samples, num_variants):
    color = sample_colors.get(sample, 'skyblue') 
    plt.bar(sample, variants, color=color)

plt.title('Number of variants per sample')
plt.xlabel('Samples')
plt.ylabel('Number of variants')
plt.xticks(rotation=45, ha='right')
plt.tight_layout() 
plt.savefig("short_v_stat.png")
