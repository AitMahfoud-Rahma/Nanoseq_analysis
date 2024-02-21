# QC_fastqc

This folder contains the scripts and files for performing quality control (QC) statistics on the FastQC results generated from the Nanoseq analysis pipeline using Nextflow.

## Purpose
The purpose of the QC_fastqc module is to analyze the quality metrics produced by FastQC and provide statistics to assess the quality of the sequencing data.


## Usage
the (. statistics.sh) command analyzes sequence quality in fastqc_data.txt files and generates a statistics.txt file containing statistics. It extracts information such as file name, number of sequences, longest sequence length, GC percentage and average quality. The script parses all fastqc_data.txt files in the subdirectories and adds the extracted statistics to the end of the (statistics.txt) file.

the code ( qlt_histo.py) uses the Matplotlib library to generate a histogram of sample quality distribution from a data file called (quality_data2.txt). Data is extracted from the file and stored in a data dictionary (data.csv). For each sample, a histogram is created with the corresponding quality and count values.

## Output


