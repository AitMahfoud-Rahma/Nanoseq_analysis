import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

data = pd.read_csv("/groups/dog/stage/rahma/deepv_cutesv/cov_sv copy.csv")
depth = data["Coverage"]
cutesv_variants = data["CuteSV"]
sniffles_variants = data["Sniffles"]
samples = data["Sample"]

# Regplot for linear regression
sns.regplot(x="Coverage", y="Sniffles", data=data, color='#C10C27')
sns.regplot(x="Coverage", y="CuteSV", data=data, color='#148F77')

# Spearman correlation 
spearman_corr, _ = spearmanr(depth, cutesv_variants)
plt.text(0.5, 0.05, f"Spearman Correlation (CuteSV): {spearman_corr:.2f}", transform=plt.gca().transAxes)

spearman_corr, _ = spearmanr(depth, sniffles_variants)
plt.text(0.5, 0.10, f"Spearman Correlation (Sniffles): {spearman_corr:.2f}", transform=plt.gca().transAxes)

for i, sample in enumerate(samples):
    plt.text(depth[i], cutesv_variants[i]+ 0.2, sample, fontsize=8, ha='right', va='bottom')


for i, sample in enumerate(samples):
    plt.text(depth[i], sniffles_variants[i]+ 0.2, sample, fontsize=8, ha='right', va='bottom')

plt.legend(labels=["Sniffles", 
                   "Sniffles Regression Line", 
                   "Sniffles Regression Field", "CuteSV", "CuteSV Regression Line", "CuteSV Regression Field"],
           fontsize='xx-small')


plt.title('Correlation between depth and number of variants detected by (Sniffles & CuteSV)', size=10)
plt.xlabel('Sequencing depth (X)')
plt.ylabel('Number of structural variants')
plt.grid(True)
plt.tight_layout()
plt.savefig("/groups/dog/stage/rahma/deepv_cutesv/corr_depth_cutesv_sniffles.png")