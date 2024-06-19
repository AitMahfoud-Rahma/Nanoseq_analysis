import sys
import csv
import gzip
import os

def process_vcf_files(directory):
    vcf_files = [file for file in os.listdir(directory) if file.endswith(".vcf.gz")]
    results = []

    for vcf_file in vcf_files:
        file_path = os.path.join(directory, vcf_file)

        variant_types = []
        variant_lengths = []

        with gzip.open(file_path, "rt") as file:
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
                            elif field.startswith("SVLEN"):
                                variant_length = int(field.split("=")[1])
                                variant_lengths.append(variant_length)

        results.append((vcf_file[:4], variant_types, variant_lengths))

    return results


def save_results_to_csv(results, output_file):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File", "Variant Type", "Variant Length"])

        for file, variant_types, variant_lengths in results:
            for variant_type, variant_length in zip(variant_types, variant_lengths):
                writer.writerow([file, variant_type, variant_length])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please specify the directory path as an argument.")
        print("Example: python sv_types.py /path/to/directory")
        sys.exit(1)

    directory = sys.argv[1]
    output_file = "/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv/sv_types_len.csv"

    results = process_vcf_files(directory)
    save_results_to_csv(results, output_file)