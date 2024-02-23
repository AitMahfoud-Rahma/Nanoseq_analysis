# Quality Control (QC) Analysis - Minimap2

## Step 1: 

Execute Script [qc.sh](qs.sh)

The `qc.sh` script performs the following operations:
- For each BAM file sorted in the directory :
  - Extracts the sample name from the file name.
  - Counts mapped and unmapped reads using Samtools ( on environment: ) .
  - Saves results to a CSV file [count_output_dna.csv] (count_output_dna.csv) in the following path
  `/groups/dog/stage/rahma/results/minimap2/analysis/QC/count_output_dna.csv`

## Step 2: Bar Plot generation

Run the  script 
```bash
Rscript qc_mapping.R
```
You will obtain this plot [qc_mappng.pdf](qc_mapping.pdf)
