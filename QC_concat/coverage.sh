#!/bin/bash


. /local/env/envsamtools-1.15.sh

DIR="/groups/dog/stage/rahma/deepv_cutesv/results/minimap2/"

for f in $DIR/*bam;do
        nbnt=$(samtools depth  $f  |  awk '{sum+=$3} END { print "Average = ",sum/NR}');
        echo $(basename $f)" " $nbnt
done
