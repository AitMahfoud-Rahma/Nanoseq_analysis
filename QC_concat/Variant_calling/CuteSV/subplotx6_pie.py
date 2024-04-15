import matplotlib.pyplot as plt

# regroupe all circular plots
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

file_names = ["AA_pie.png", "AB_pie.png", "AC_pie.png", "AD_pie.png", "AE_pie.png", "AF_pie.png"]
for i, ax in enumerate(axs.flat):
    if i < len(file_names):
        image_path = file_names[i]
        img = plt.imread(image_path)
        ax.imshow(img)
        ax.axis('off')  # Désactiver les axes
        #ax.set_title(image_path[:-8])  # Titre sans l'extension de fichier

fig.suptitle('Variant types by CuteSV', fontsize=24)
plt.tight_layout()

plt.savefig("subplotx6_pie.png")
