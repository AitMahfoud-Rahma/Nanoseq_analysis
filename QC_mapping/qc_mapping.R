library(ggplot2)
library(dplyr)
library(scales)


csvfile <- read.csv("/groups/dog/stage/rahma/results/minimap2/analysis/QC/count_output_dna.csv", header=FALSE)

# Renamme columns
colnames(csvfile) <- c("sample_type", "count")

# Extract type (mapped or unmapped) &  sample name from file name 
csvfile <- dplyr::mutate(csvfile, sample = strsplit(sample_type, split="-unmapped|-mapped")) %>%
  dplyr::mutate(type = ifelse(endsWith(sample_type, "-mapped"), "mapped", "unmapped")) %>%
  dplyr::select(-sample_type)

csvfile$sample <- as.character(csvfile$sample)
csvfile$type <- as.factor(csvfile$type)

# Create a supperposed plot for mapped and unmapped reads
plot <- ggplot(csvfile, aes(fill=type, y=count, x=sample)) + 
  geom_bar(width=0.95, position="stack", stat="identity") +
  geom_text(aes(label = count), position = position_stack(vjust = 0.5), size = 3) +
  labs(fill="Type", x="Samples", y="Number of Reads") +
  ggtitle("Distribution of Mapped and Unmapped Reads") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))+theme(plot.title = element_text(hjust = 0.5))
# Save a plot on .pdf file
ggsave("/groups/dog/stage/rahma/results/minimap2/analysis/QC/qc_mapping.pdf", plot, width=10, height=7)
