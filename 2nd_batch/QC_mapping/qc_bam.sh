#!/bin/bash
. /local/env/envsamtools-1.15.sh

# Define directories
temp_directory=$(mktemp -d)
bam_directory="/groups/dog/stage/rahma/2nd_batch/results/minimap2"
output_csv="/groups/dog/stage/rahma/2nd_batch/results/minimap2/qc_mapping.csv"

# Check if input directory exists
if [ ! -d "$bam_directory" ]; then
    echo "Error: Input directory $bam_directory does not exist"
    exit 1
fi

# Loop through BAM files
for bam_file in "$bam_directory"/*_R1.sorted.bam; do
    # Exclude .bai files
    if [[ "$bam_file" == *.bai ]]; then
        continue
    fi
    
    # Extract sample name
    sample_name=$(basename "$bam_file" | sed 's/_R1\.sorted\.bam//')

    # Count mapped and unmapped reads
    samtools view -c -F 260 "$bam_file" > "$temp_directory/tmp-$sample_name-mapped.txt"
    samtools view -c -f 4 "$bam_file" > "$temp_directory/tmp-$sample_name-unmapped.txt"

    # Append results to CSV
    echo "$sample_name-mapped,$(cat "$temp_directory/tmp-$sample_name-mapped.txt")" >> "$output_csv"
    echo "$sample_name-unmapped,$(cat "$temp_directory/tmp-$sample_name-unmapped.txt")" >> "$output_csv"
done

# Clean up temporary files
rm -rf "$temp_directory"

