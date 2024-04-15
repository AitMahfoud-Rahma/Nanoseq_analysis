import csv
import gzip
import os
from collections import Counter
# directory which countains .vcf files
directory = "/groups/dog/stage/rahma/deepv_cutesv/results/variant_calling/cutesv"

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

output_file = "/groups/dog/stage/rahma/deepv_cutesv/results/variant_calling/cutesv/sv_types.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["File", "Variant Type", "Count"]) 

    for file, type_counts in results:
        for variant_type, count in type_counts.items():
            writer.writerow([file, variant_type, count])
