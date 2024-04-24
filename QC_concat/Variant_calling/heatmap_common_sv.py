import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Dict to store for each sample number of common variants  
data = {
    "AD": [25, 1, 0, 0, 0, 0],
    "AA": [1, 13, 0, 2, 1, 1],
    "AB": [0, 0, 14, 0, 0, 0],
    "AE": [0, 2, 0, 13, 1, 1],
    "AC": [0, 1, 0, 1, 16, 1],
    "AF": [0, 1, 0, 1, 1, 27]}

# DataFrame with samples name
df = pd.DataFrame(data, index=data.keys())

# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt='d', cmap='Blues')
plt.title('Common variants between samples')
plt.xlabel('Samples')
plt.ylabel('Samples')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()


plt.savefig('/groups/dog/stage/rahma/deepv_cutesv/results/heatmap_common_sv.png')