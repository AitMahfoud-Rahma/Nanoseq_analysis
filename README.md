# Nanoseq Analysis for GOLDOG Longevity Project

This repository contains a Nextflow pipeline for Nanoseq analysis applied to long-read data ( DNA , Blue line) for the GOLDOG longevity project (1st batch).

![Capture d’écran 2024-04-16 à 15 41 08](https://github.com/AitMahfoud-Rahma/Nanoseq_analysis/assets/155021211/1763f124-4706-4f57-a676-9054870aeb96)

## Prerequisites

Before running the Nextflow command, make sure to perform the following steps:

### 1. Create an input file (samplesheet.csv)

Create a file named [samplesheet.csv](samplesheet.csv) with the following information:

```csv
group,replicate,barcode,input_file,fasta,gtf
```
### 2. Choose a compute cluster node

Use the following command to request a node on the compute cluster:
```srun --pty --cpus-per-task=12 --mem=100G bash```

### 3. Running the Nanoseq Nextflow Pipeline

Execute the following command to run the Nanoseq Nextflow pipeline:
```nextflow run nf-core/nanoseq \
  --input samplesheet.csv \
  --protocol DNA \
  --skip_quantification \
  --skip_demultiplexing \
  -profile singularity
```
  - **--input samplesheet.csv** : specifies the input file.
  - **--protocol DNA**: indicates the DNA analysis protocol.
  - **--skip_quantification**: skips the quantification step.
  - **--skip_demultiplexing**: skips the demultiplexing step.
  - **-profile singularity**: uses the Singularity profile for execution.

Ensure that Nextflow is installed, and Singularity is available on your cluster before running the command.

## Output
The pipeline generates the following output directories:

  - **fastqc**: FastQC reports for input and output files.
  - **minimap2**: Minimap2 alignment results.
  - **multiqc**: MultiQC report summarizing the analysis.
  - **nanoplot**: NanoPlot reports for input and output files.
  - **pipeline_info**: Information about the pipeline.
  - **variant_calling**: zipped VCF file with smtructural variants.

## Analysis

- [QC_fastqc](QC_fastqc) : Statistical analysis of quality for the sequences resulting from FastQC.
- [QC_mapping](QC_mapping) : QC_mapping: Statistical analysis of quality for the alignment results with the reference genome.
- [QC_concat](QC_concat) : Analysis of concatenated 1st batch data.
- 

# Environment Path & Versions

- R: `/local/env/envr-4.1.3.sh`
- samtools: `/local/env/envsamtools-1.15.sh`
- Python: `/local/env/envpython-3.9.5.sh`
- Pipeline_info :
  ```bash
  BEDTOOLS_GENOMECOV:
  bedtools: 2.29.2
  CUSTOM_DUMPSOFTWAREVERSIONS:
    python: 3.10.6
    yaml: '6.0'
  CUTESV:
  cuteSV: 1.0.12
  DEEPVARIANT:
    deepvariant: 1.4.0
  GET_CHROM_SIZES:
    samtools: '1.13'
  MINIMAP2_INDEX:
    minimap2: 2.17-r941
  SAMTOOLS_STATS:
    samtools: 1.16.1
  SNIFFLES:
    sniffles: 1.0.12
  UCSC_BEDGRAPHTOBIGWIG:
    ucsc_bedgraphtobigwig: '377'
  Workflow:
    Nextflow: 23.10.0
    nf-core/nanoseq: 3.1.0

# First batch details 
![Capture d’écran 2024-04-16 à 16 08 55](https://github.com/AitMahfoud-Rahma/Nanoseq_analysis/assets/155021211/66a8edb8-1e38-4dab-a8c5-07cd48c4837f)


