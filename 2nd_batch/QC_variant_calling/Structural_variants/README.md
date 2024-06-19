The [sv_types.py](sv_types.py) script is used to analyze vcf.gz files located in a specified directory. It extracts variant types (SVTYPE) from lines with “PASS” status, and counts the number of occurrences of each variant type. The results are then saved in a CSV file with the columns “File”, “Variant Type” and “Count”.

# Common Structurals variants 
After obtaining all the (.vcf) files from CuteSV or Sniffles to have the common variants, the following steps should be followed.

1. Load the bcftools-1.9.sh environment.
 
2. Execute the following command: 
```bcftools isec -c all -p dir -n=2 A.vcf.gz B.vcf.gz```

The output of this command will be a directory named "**dir**" containing three files:
     
    - 0000.vcf 
    - 0001.vcf
    - 0002.vcf


- The **0000.vcf** file represents the variants present in file A but not in file B.
- The **0001.vcf** file represents the variants present in B but not in A. 
- The **0002.vcf** file contains the variants present in both A and B. 

# Sniffles Errors

When using Sniffles, the job often finishes with formatting errors in the generated VCF file. 
This prevents bcftools from manipulating the file directly. Therefore, a manual reformatting process needs to be implemented. This involves adding information to the Sniffles VCF file header and/or removing non-PASS variants from the VCF file.
Once the reformatting is done, the VCF files should be sorted using bcftools sort. Afterward, the VCF file needs to be transformed into the bgzip format using the bgzip command. This file will then be indexed by bcftools index with the "-tbi" option. Once the .vcf.gz.tbi files are obtained, the bcftools isec command can be executed.

eg. for BB-1 file :
1.  ```awk '$0 ~ /^#/ || $7 == "PASS"' BB-1_R1_sniffles.vcf > BB-1.vcf```
2. ```bcftools sort BB-1.vcf > BB-1_sorted.vcf```
3. ```bgzip BB-1_sorted.vcf```
4. ```bcftools index --tbi BB-1_sorted.vcf.gz ```.

