# Nanoseq_analysis

the (. statistics.sh) command analyzes sequence quality in fastqc_data.txt files and generates a statistics.txt file containing statistics. It extracts information such as file name, number of sequences, longest sequence length, GC percentage and average quality. The script parses all fastqc_data.txt files in the subdirectories and adds the extracted statistics to the end of the (statistics.txt) file.

the code ( qlt_histo.py) uses the Matplotlib library to generate a histogram of sample quality distribution from a data file called (quality_data2.txt). Data is extracted from the file and stored in a data dictionary (data.csv). For each sample, a histogram is created with the corresponding quality and count values.


# Environment Path & Versions

- R: `/local/env/envr-4.1.3.sh`
- samtools: `/local/env/envsamtools-1.15.sh`
- Python: `/local/env/envpython-3.9.5.sh`
