import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#for sniffles
#data = pd.read_csv("/groups/dog/stage/rahma/2nd_batch/results/variant_calling/sniffles_before_sort/sv_types.csv")
#for CuteSV
data = pd.read_csv("/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/sv_types.csv")
# Dict for legends color 
colors_dict = {
    'DEL': '#e0b5b6',
    'INS': '#a5c4bc',
    'DUP': '#95a0b3',
    'BND': '#ae7577',
    'INVDUP': "#FF5733",
    'DEL/INV': "#E3E364",
}


for file_name in data['File'].unique():
    file_data = data[data['File'] == file_name]
    counts = file_data['Count'].values
    labels = file_data['Variant Type'].values

    percentages = np.round(counts / np.sum(counts) * 100, 1)
    
    #output_file = f"{file_name}_sniffles_pie.png"
#for cuteSV
    output_file = f"{file_name}_CuteSV_pie.png"

    plt.figure()

    # Obtain color for each type
    colors = [colors_dict.get(variant, 'gray') for variant in labels]
    wedges, texts = plt.pie(counts, colors=colors, startangle=140)

    # Cercle annotation %
    for i, (w, label, pct) in enumerate(zip(wedges, labels, percentages)):
        if label in ['INS', 'DEL']:
            angle = (w.theta2 - w.theta1)/2 + w.theta1
            x = 0.6 * np.cos(np.radians(angle))
            y = 0.6 * np.sin(np.radians(angle))
            plt.text(x, y, f"{pct}%", ha='center', va='center', color='black', fontsize='small')

    # Legend labes
    legend_labels = [f"{v} ({c})" for v, c in zip(labels, counts)]
    plt.legend(wedges, legend_labels, loc="lower center", bbox_to_anchor=(0.8, -0.2),
               title="Variant Types", ncol=2, fontsize='small')

    plt.title(file_name)

    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
