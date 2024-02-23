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
csvfile$type <- factor(csvfile$type) # convert type en factor

# Calculate % of mapped/unmapped reads 
csvfile <- csvfile %>%
  group_by(sample) %>%
  mutate(total_reads = sum(count),
         percentage = count / total_reads * 100)
         dog = substr(sample, 1, 2)) # add column which contain only first 2 letters of samples name

plot <- ggplot(csvfile, aes(fill = dog, alpha = type, y = count, x = sub("_R1", "-Barcode", sample), group = dog, label = paste0(round(percentage, 2)))) +
  geom_bar(width = 0.95, position = "stack", stat = "identity") +
  scale_alpha_manual(values = c(1, 0.5), name = "Read proportion (%)") +
  coord_flip() +
  #labs(alpha = "Read proportion (%)", fill = "Dog") +
  guides(alpha = guide_legend(order = 2), fill = guide_legend(order = 1)) +
  xlab("Samples") +
  ylab("Number of Reads (k)") +
  geom_text(size = 3, position = position_stack(vjust = 0.15), show.legend = FALSE) +
  scale_y_continuous(labels = scales::label_number(scale = 1e-3), breaks = scales::pretty_breaks(n = 6)) +
                     #(labels = scales::label_number(scale = 1e-3, suffix = "k", size = 50))
  scale_fill_manual(values = c("#DD72A7", "#AA72DD", "#447FBE", "#5FAEE8", "#44BE8A", "#A0BE44"), name = "Dog") +
  ggtitle("Distribution of Mapped and Unmapped Reads") +
  annotate("text", x = 6, y = max(csvfile$count), hjust = 0.95, vjust = 2,
           label = "AA = Bernese mountain dog\nAB = Bernese mountain dog\nAC = Greater Swiss Mountain dog\nAD = Leonberger dog\nAE = Beauceron\nAF = Pyrenean Sheep dog")+
  theme_bw() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 18),
    axis.title.x = element_text(size = 18),
    axis.title.y = element_text(size = 18),
    axis.text.x = element_text(size = 17),
    legend.title = element_text(size = 15),
    legend.text = element_text(size = 15)
  )

ggsave("/groups/dog/stage/rahma/results/minimap2/analysis/QC/qc_mapping.pdf", plot, width = 12, height = 7)
