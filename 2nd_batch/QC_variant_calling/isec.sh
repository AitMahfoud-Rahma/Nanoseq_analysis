#!/bin/bash

# Specifie directory for .vcf.gz files
directory="/groups/dog/stage/rahma/2nd_batch/results/variant_calling/cutesv"

# Liste all vcf files
files=("$directory"/*.vcf.gz)

# for each two files ( eg. AA, AB)
for ((i = 0; i < ${#files[@]}; i++)); do
    for ((j = i + 1; j < ${#files[@]}; j++)); do
        vcf_file1="${files[$i]}"
        vcf_file2="${files[$j]}"
        
        # check if .vcf.gz files have their .tbi 
        if [ -f "${vcf_file1}.tbi" ] && [ -f "${vcf_file2}.tbi" ]; then
            # Exécute bcftools isec to find common variants
            output_dir="${vcf_file1%.vcf.gz}_vs_${vcf_file2%.vcf.gz}"
            mkdir -p "$output_dir"
            bcftools isec -p "$output_dir" "$vcf_file1" "$vcf_file2"
        else
            echo "One of these files (${vcf_file1} or ${vcf_file2}) are not indexed. Please think to index .vcf.gz files with tabix."
        fi
    done
done
