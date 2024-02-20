import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = []

with open("gc_content_data.txt", "r") as file:
    current_directory = None

    for line in file:
        line = line.strip()

        if line.startswith("Directory:"):
            current_directory = line.split(":")[1].strip()
        elif line.startswith("#GC Content") or line.startswith(">>"):
            continue
        else:
            values = line.split("\t")
            if len(values) >= 2:
                gc_content = float(values[0])
                count = float(values[1])
                data.append({"Directory": current_directory, "GC Content": gc_content, "Count": count})

data = pd.DataFrame(data)
data.to_csv("data_gc.csv", index=False)

palette = sns.color_palette("Set3", n_colors=len(data["Directory"].unique()))

plt.figure(figsize=(12, 6))
sns.violinplot(x="Directory", y="GC Content", data=data, inner=None, palette=palette)
sns.boxplot(x="Directory", y="GC Content", data=data, width=0.4, boxprops={"facecolor":"None"})
sns.stripplot(x="Directory", y="GC Content", data=data, size=3, color="#9DDEFA")
plt.title("Distribution of GC Content per sample")
plt.xlabel("Samples")
plt.ylabel("GC Content")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('gc_content_violin.png')
