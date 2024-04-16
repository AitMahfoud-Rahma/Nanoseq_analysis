# Nanoseq Analysis for GOLDOG Longevity Project

This repository contains a Nextflow pipeline for Nanoseq analysis applied to long-read data for the GOLDOG longevity project (2nd Batch).
![Capture d’écran 2024-04-16 à 15 31 22](https://github.com/AitMahfoud-Rahma/Nanoseq_analysis/assets/155021211/31b3f8d8-41fb-4348-9d1a-60a7acb958a0)


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
```time nextflow run nf-core/nanoseq -r 3.1.0 \
--input '/groups/dog/stage/rahma/2nd_batch/samplesheet.csv' \
--protocol DNA --skip_quantification --skip_demultiplexing \
--call_variants --structural_variant_caller 'sniffles' \
--variant_caller 'deepvariant' -profile singularity
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
- [QC_nanoplot](QC_nanoplot) : QC_nanoplot: Statistical analysis of quality for the nanoseq results.
- [QC_variant_calling](QC_variant_calling) : QC_variant_calling: Statistical analysis of quality for the short variants annotation with [Deepvariant](2nd_batch/QC_variant_calling/Short_variants/Deepvariant), and the structural variants
  with [Sniffles](2nd_batch/QC_variant_calling/Structural_variants/Sniffles) & [CuteSV](2nd_batch/QC_variant_calling/Structural_variants/CuteSV).

# Environment Path & Versions

- R: `/local/env/envr-4.1.3.sh`
- samtools: `/local/env/envsamtools-1.15.sh`
- Python: `/local/env/envpython-3.9.5.sh`
- pipeline_info :

```bash

```



