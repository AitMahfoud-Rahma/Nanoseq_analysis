import sys
import csv
import gzip
import os
from collections import Counter

def process_vcf_files(directory):
    vcf_files = [file for file in os.listdir(directory) if file.endswith(".vcf.gz")]
    results = []

    for vcf_file in vcf_files:
        file_path = os.path.join(directory, vcf_file)
        
        variant_types = []

        with gzip.open(file_path, "rt") as file:
            for line in file:
                if not line.startswith("#"):
                    fields = line.strip().split("\t")
                    info = fields[7]
                    info_fields = info.split(";")
                    for field in info_fields:
                        if field.startswith("SVTYPE"):
                            variant_type = field.split("=")[1]
                            variant_types.append(variant_type)

        type_counts = Counter(variant_types)
        results.append((vcf_file[:2], type_counts))

    return results

def save_results_to_csv(results, output_file):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File", "Variant Type", "Count"]) 

        for file, type_counts in results:
            for variant_type, count in type_counts.items():
                writer.writerow([file, variant_type, count])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please specify the directory path as an argument.")
        print("Example: python sv_types.py /path/to/directory")
        sys.exit(1)

    directory = sys.argv[1]
    output_file = "sv_types.csv"

    results = process_vcf_files(directory)
    save_results_to_csv(results, output_file)

# python sv_types.py /groups/dog/stage/rahma/deepv_cutesv/results/variant_calling/sniffles
