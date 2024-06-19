import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import LogNorm


data = {
    "AL": [1391, 6, 44, 95, 12, 4],
    "BB-1": [6, 378, 23, 32, 15, 2],
    "BB-2": [44, 23, 24467, 2482, 114, 3],
    "BB-3": [95, 32, 2482, 78269, 197, 1],
    "BB-4": [12, 15, 114, 197, 1890, 2],
    "BE": [4, 2, 3, 1, 2, 59]
}

df = pd.DataFrame(data, index=data.keys())
# Hide half of heatmap
mask = np.triu(np.ones_like(df, dtype=bool), k=1)

custom_cmap = sns.color_palette("coolwarm", as_cmap=True)

plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt='d', cmap=custom_cmap, mask=mask, norm=LogNorm(vmin=1, vmax=df.values.max()))
plt.title('Common structural sariants between samples')
plt.xlabel('Samples')
plt.ylabel('Samples')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

plt.savefig('/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/heatmap_common_sv.png')
plt.show()
