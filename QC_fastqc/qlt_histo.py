import matplotlib.pyplot as plt
import numpy as np

file_path = "quality_data2.txt"

data = {}
current_sample = None

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith("Directory: "):
            current_sample = line.strip().split(": ")[1]
            data[current_sample] = {"Quality": [], "Count": []}
        elif line.startswith("#Quality") or line.startswith(">>END_MODULE"):
            continue
        elif current_sample and line.strip():
            values = line.strip().split()
            if len(values) == 2:
                try:
                    quality, count = int(values[0]), float(values[1])
                    data[current_sample]["Quality"].append(quality)
                    data[current_sample]["Count"].append(count)
                except ValueError:
                    print(f"Ignoring invalid data in {current_sample}: {line}")

# color palette
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
num_samples = len(data)
num_rows = num_samples // 2 + num_samples % 2  # Ensure an even number of rows for a 2x2 grid
num_cols = 2

# arrange subplots in a dynamic grid
fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 8 * num_rows), sharex=True)
axs = axs.flatten()

for i, (sample, values) in enumerate(data.items()):
    axs[i].hist(values["Quality"], bins=range(min(values["Quality"]), max(values["Quality"]) + 1),
                weights=values["Count"], edgecolor='black', alpha=0.7, color=colors[i])
    axs[i].set_title(f"{sample}", fontsize=14)
    axs[i].set_ylabel("Count", fontsize=12)
    axs[i].grid(True, linestyle='--', alpha=0.7)

# Add common x-axis label
if num_samples > 1:
    axs[-2].set_xlabel("Quality", fontsize=12)
    axs[-1].set_xlabel("Quality", fontsize=12)
else:
    axs[0].set_xlabel("Quality", fontsize=12)

# Add legend if multiple samples
if num_samples > 1:
    axs[0].legend(data.keys(), loc='upper right')

plt.suptitle("Quality Distribution Across Samples", fontsize=16, y=0.95)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('qlt_histo.png')
