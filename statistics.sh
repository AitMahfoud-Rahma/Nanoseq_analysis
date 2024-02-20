#!/bin/bash

# Quality function
calculate_quality() {
   awk '/>>Per sequence quality scores/{flag=1; next} /^>>END_MODULE/{flag=0} flag && /^[0-9-]+/ {sum += $1 * $2; count += $2} END {if (count > 0) print sum/count; else print "N/A"}'
}


# echo header
echo -e "Filename\tNb-Sequences\tLongest_Sequence\tGC-Percentage\tQuality" > statistics.txt

# The extract function
extract_info() {
    file="$1"
    filename=$(grep "Filename" "$file" | cut -f 2)
    total_sequences=$(grep "Total Sequences" "$file" | cut -f 2)
    sequence_length=$(grep "Sequence length" "$file" | cut -f 2 | awk -F'-' '{print $2}')
    quality=$(calculate_quality < "$file")
    gc_percentage=$(grep "%GC" "$file" | cut -f 2)

    echo -e "$filename\t$total_sequences\t$sequence_length\t$gc_percentage\t$quality" >> statistics.txt
}

# Apply function for each field
for file in */fastqc_data.txt; do
    extract_info "$file"
done
