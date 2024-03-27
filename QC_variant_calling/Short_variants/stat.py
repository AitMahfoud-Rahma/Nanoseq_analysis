import os
import gzip

dir = "/groups/dog/stage/rahma/results/variant_calling/deepvariant"
output_file = "short_variants_stat.txt"

def count_line_file(file):
    with gzip.open(file, 'rt') as f:
        nb_lines = sum(1 for line in f)
    return nb_lines
  
samples = sorted([file.split("_")[0] for file in os.listdir(dir) if file.endswith(".vcf.gz") and not file.endswith(".g.vcf.gz")])

with open(output_file, 'w') as out_file:
    out_file.write("Sample\tNumber of variants\n")
    for sample in samples:
        file = f"{sample}_R1.vcf.gz"
        path = os.path.join(dir, file)
        nb_lines = count_line_file(path)
        out_file.write(f"{sample}\t{nb_lines}\n")
