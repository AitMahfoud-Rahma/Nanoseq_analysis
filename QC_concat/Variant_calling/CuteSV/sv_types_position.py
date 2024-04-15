import csv
import gzip
import os
from collections import Counter

directory = "/groups/dog/stage/rahma/deepv_cutesv/results/variant_calling/cutesv"

vcf_files = [file for file in os.listdir(directory) if file.endswith(".vcf.gz")]

results = []

for vcf_file in vcf_files:
    file_path = os.path.join(directory, vcf_file)
    
    variant_info = []

    with gzip.open(file_path, "rt") as file:
        for line in file:
            if not line.startswith("#"):
                fields = line.strip().split("\t")
                chromosome = fields[0]
                position = fields[1]
                info = fields[7]
                info_fields = info.split(";")
                variant_type = None
                for field in info_fields:
                    if field.startswith("SVTYPE"):
                        variant_type = field.split("=")[1]
                        break  # On arrête dès qu'on a trouvé le type de variante
                if variant_type:
                    variant_info.append((chromosome, position, variant_type))

    type_counts = Counter(variant_info)
    results.append((vcf_file[:2], type_counts))

output_file = "/groups/dog/stage/rahma/deepv_cutesv/results/variant_calling/cutesv/sv_types&position.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["File", "Chromosome", "Position", "Variant Type", "Count"]) 

    for file, type_counts in results:
        for variant_info, count in type_counts.items():
            chromosome, position, variant_type = variant_info
            writer.writerow([file, chromosome, position, variant_type, count])
