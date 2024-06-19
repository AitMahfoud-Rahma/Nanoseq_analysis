import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("sv_types_len.csv")

# List of samples
samples = ["BB-1", "BB-2", "BB-3", "BB-4", "AL_R", "BE_R"]

# Go through each sample and plot the histogram
for sample in samples:
    # Filter data for the given sample
    sample_data = data[data["File"] == sample]

    # Transforming negative deletion values into positive values
    sample_data["Variant Length"] = sample_data["Variant Length"].abs()

    # Plot the histogram of variant lengths for each type of variant
    plt.figure(figsize=(8, 6))
    sns.histplot(data=sample_data, x="Variant Length", hue="Variant Type", multiple="stack", palette="husl")

    plt.xlim(0, 2500)

    plt.xlabel("Variant Length (bp)")
    plt.ylabel("Number of SVs")
    plt.title(f"Distribution of Structural Variant Lengths - {sample}")

    # save plot
    plt.savefig(f"{sample}_histogram.png")
