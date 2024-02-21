#!/bin/bash


temp_directory=~/my_temp_directory
mkdir -p $temp_directory

# Path to BAM directory
bam_directory="/groups/dog/stage/rahma/results/minimap2"

# For each bam file in directory
for bam_file in $bam_directory/*.sorted.bam; do
    # Extract file name ( which contains sample name ex: AA-1_R1)
    sample_name=$(basename "$bam_file" | cut -d'.' -f1)

    # Count mapped reads
    samtools view -F 260 "$bam_file" | awk '{ print $1 }' | sort -n | uniq | wc -l > "$temp_directory/tmp-$sample_name-mapped.txt"

    # Count unmapped reads
    samtools view -c -f 4 "$bam_file" > "$temp_directory/tmp-$sample_name-unmapped.txt"

    # print information in tmp into .csv files
    echo "$sample_name-mapped,"$(cat "$temp_directory/tmp-$sample_name-mapped.txt") >> "/groups/dog/stage/rahma/results/minimap2/analysis/QC/count_output_dna.csv"
    echo "$sample_name-unmapped,"$(cat "$temp_directory/tmp-$sample_name-unmapped.txt") >> "/groups/dog/stage/rahma/results/minimap2/analysis/QC/count_output_dna.csv"
done

