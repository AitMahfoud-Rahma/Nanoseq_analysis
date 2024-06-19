import pandas as pd
import matplotlib.pyplot as plt

input_file = "/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/nb_sv.txt"

# Read the data into a pandas DataFrame, skipping the first row
data = pd.read_csv(input_file, sep='\t', header=None, names=['sample', 'total', 'pass_variants'], skiprows=1)

# Convert the columns to numeric
data['total'] = pd.to_numeric(data['total'], errors='coerce')
data['pass_variants'] = pd.to_numeric(data['pass_variants'], errors='coerce')

# Remove rows with missing values
data = data.dropna()

# Calculate the percentage of PASS variants relative to the total
data['pass_percentage'] = (data['pass_variants'] / data['total']) * 100

# Create a normalized bar plot with a logarithmic scale on the y-axis
plt.figure(figsize=(10, 6))
bars = plt.bar(data['sample'], data['total'], color='orange', label='Total Variants')

# Add annotations to display the percentage of PASS variants relative to the total
for bar, percentage in zip(bars, data['pass_percentage']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + -8, f'{percentage:.2f}%', ha='center')

pass_bars = plt.bar(data['sample'], data['pass_variants'], color='skyblue', label='PASS Variants')

plt.xlabel('Samples')
plt.ylabel('Number of Variants (log scale)')
plt.title('Number of Structural Variants identified by CuteSV')
plt.legend()
plt.xticks(rotation=45)
plt.yscale('log')  # Use a logarithmic scale on the y-axis
plt.tight_layout()
plt.savefig("/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/Nb_SV_log_scale.png")
plt.show()