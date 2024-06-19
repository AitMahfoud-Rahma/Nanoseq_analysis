import os
import gzip

dir = "/groups/dog/stage/rahma/2nd_batch/results/variant_calling/deepvariant"
output_file = "/groups/dog/stage/rahma/2nd_batch/results/variant_calling/deepvariant/nb_shortv.txt"

def count_line_file(file):
    with gzip.open(file, 'rt') as f:
        nb_lines_total = 0
        nb_short_variants = 0
        for line in f:
            if not line.startswith('##') and not line.startswith('#'):
                nb_lines_total += 1
                columns = line.split('\t')
                if columns[6] == 'PASS': 
                    nb_short_variants += 1
    return nb_lines_total, nb_short_variants
  
samples = sorted([file.split("_")[0] for file in os.listdir(dir) if file.endswith(".vcf.gz") and not file.endswith(".g.vcf.gz")])

with open(output_file, 'w') as out_file:
    out_file.write("Sample\tNumber of total variants\tNumber of short variants\n")
    for sample in samples:
        file = f"{sample}_R1.vcf.gz"
        path = os.path.join(dir, file)
        nb_total, nb_short  = count_line_file(path)
        out_file.write(f"{sample}\t{nb_total}\t{nb_short}\n")
