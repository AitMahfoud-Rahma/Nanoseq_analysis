import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

data = pd.read_csv("/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/depth_cutesv_sniffles.csv")
depth = data["Depth"]
cutesv_variants = data["CuteSV"]
sniffles_variants = data["Sniffles"]
samples = data["Sample"]

# Calculate Spearman correlation for Sniffles
spearman_corr_sniffles, _ = spearmanr(depth, sniffles_variants, nan_policy='omit')

# Calculate Spearman correlation for CuteSV
spearman_corr_cutesv, _ = spearmanr(depth, cutesv_variants)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Regplot for linear regression - Sniffles
sns.regplot(x="Depth", y="Sniffles", data=data, color='#C10C27', ax=ax1)
ax1.set_title('Correlation between depth and number of variants detected by Sniffles', size=10)
ax1.set_xlabel('Sequencing depth (X)')
ax1.set_ylabel('Number of structural variants')
ax1.grid(True)
ax1.set_xlim(0, 40)

# Spearman correlation - Sniffles
ax1.text(0.5, 0.95, f"Spearman Correlation (Sniffles): {spearman_corr_sniffles:.2f}", transform=ax1.transAxes)

# Annotate samples for Sniffles
for i, sample in enumerate(samples):
    ax1.text(depth[i], sniffles_variants[i]+0.2, sample, fontsize=8, ha='right', va='bottom')

# Regplot for linear regression - CuteSV
sns.regplot(x="Depth", y="CuteSV", data=data, color='#148F77', ax=ax2)
ax2.set_title('Correlation between depth and number of variants detected by CuteSV', size=10)
ax2.set_xlabel('Sequencing depth (X)')
ax2.set_ylabel('Number of structural variants')
ax2.grid(True)
ax2.set_xlim(0, 40)

# Spearman correlation - CuteSV
ax2.text(0.5, 0.95, f"Spearman Correlation (CuteSV): {spearman_corr_cutesv:.2f}", transform=ax2.transAxes)

# Annotate samples for CuteSV
for i, sample in enumerate(samples):
    ax2.text(depth[i], cutesv_variants[i]+0.2, sample, fontsize=8, ha='right', va='bottom')

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig("/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/corr_depth_cutesv_sniffles.png")
