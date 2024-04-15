import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("sv_types.csv")

for file_name in data['File'].unique():
    file_data = data[data['File'] == file_name]
    counts = file_data['Count'].values
    percentages = np.round(counts / np.sum(counts) * 100, 1)
    labels = [f"{v} ({p} %)" for v, p in zip(file_data['Variant Type'], percentages)]

    output_file = f"{file_name}_pie.png"
    colors = plt.cm.Blues(np.linspace(0.2, 1, len(counts)))

    plt.figure()
    plt.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(file_name)

    # la légende
    plt.legend(file_data['Variant Type'], loc="center left", bbox_to_anchor=(1, 0.5), title="Variant Type")

    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
