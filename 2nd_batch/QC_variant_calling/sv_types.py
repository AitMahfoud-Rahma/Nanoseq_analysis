import sys
import csv
from collections import Counter

def process_vcf_file(file_path):
    variant_types = []

    with open(file_path, "rt") as file:
        for line in file:
            if not line.startswith("#"):
                fields = line.strip().split("\t")
                info = fields[7]
                info_fields = info.split(";")
                if fields[6] == 'PASS':
                    for field in info_fields:
                        if field.startswith("SVTYPE"):
                            variant_type = field.split("=")[1]
                            variant_types.append(variant_type)
    
    type_counts = Counter(variant_types)
    return type_counts
    

def save_results_to_csv(type_counts, output_file):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Variant Type", "Count"]) 

        for variant_type, count in type_counts.items():
            writer.writerow([variant_type, count])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please specify the VCF file path as an argument.")
        print("Example: python sv_types.py /path/to/file.vcf.gz")
        sys.exit(1)

    file_path = sys.argv[1]
    output_file = "sv_types.csv"

    type_counts = process_vcf_file(file_path)
    save_results_to_csv(type_counts, output_file)
