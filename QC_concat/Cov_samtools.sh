#!/bin/bash
# AIT MAHFOUD Rahma 
# Script to calculate the % of coverage using samtools coverage
. /local/env/envsamtools-1.15.sh

DIR="/groups/dog/stage/rahma/deepv_cutesv/results/minimap2/"

for f in $DIR/*.bam; do
    coverage=$(samtools coverage "$f" | awk 'NR > 1 {sum += ($6 * $3); count += $3} END {if (count > 0) {percentage = (sum / count); printf "Coverage %% : %.2f%%\n", percentage}}')
    echo "$(basename "$f") $coverage"
done
