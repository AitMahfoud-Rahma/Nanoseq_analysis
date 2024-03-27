import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm

output_file = "short_variants_stat.txt" # this is the output file of (stat.py)

samples = []
num_variants_total = []
num_variants_pass = []

with open(output_file, 'r') as file:
    next(file)  
    for line in file:
        sample, total, pass_variants = line.strip().split('\t')
        samples.append(sample)
        num_variants_total.append(int(total))
        num_variants_pass.append(int(pass_variants))


plt.figure(figsize=(10, 6))
x = range(len(samples))
bar_width = 0.35
plt.bar(x, num_variants_total, bar_width, label='Total Variants')
plt.bar([i + bar_width for i in x], num_variants_pass, bar_width, label='Variants PASS')
plt.title('Number of variants per sample')
plt.xlabel('Samples')
plt.ylabel('Number of variants')
plt.xticks([i + bar_width / 2 for i in x], samples, rotation=45, ha='right')
plt.legend()
plt.tight_layout() 
plt.savefig("short_v_stat.png")
