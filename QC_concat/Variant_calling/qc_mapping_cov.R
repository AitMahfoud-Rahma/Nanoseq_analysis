library(ggplot2)
library(dplyr)
library(scales)

csvfile <- read.csv("/groups/dog/stage/rahma/deepv_cutesv/results/count_output_dna_cov.csv", header=FALSE)
colnames(csvfile) <- c("sample_type", "count", "coverage")  # Nommer la troisième colonne "coverage"

csvfile <- dplyr::mutate(csvfile, sample = gsub("-unmapped|-mapped", "", sample_type)) %>%
  dplyr::mutate(type = ifelse(endsWith(sample_type, "-mapped"), "mapped", "unmapped")) %>%
  dplyr::select(-sample_type)

csvfile$sample <- as.character(csvfile$sample)
csvfile$type <- factor(csvfile$type)

csvfile <- csvfile %>%
  group_by(sample) %>%
  mutate(total_reads = sum(count),
         percentage = count / total_reads * 100)

plot <- ggplot(csvfile, aes(fill = substr(sample, 1, 2), alpha = type, y = count, x = sample, group = sample, label = paste0(round(percentage, 2)))) +
  geom_bar(width = 0.95, position = "stack", stat = "identity", aes(size = coverage)) +
  scale_alpha_manual(values = c(1, 0.5), name = "Read proportion (%)") +
  coord_flip() +
  guides(alpha = guide_legend(order = 2), fill = guide_legend(order = 1)) +
  xlab("Samples") +
  ylab("Number of Reads (k)") +
  geom_text(size = 3, position = position_stack(vjust = 0.15), show.legend = FALSE) +
  scale_y_continuous(labels = scales::label_number(scale = 1e-3), breaks = scales::pretty_breaks(n = 6)) +
  scale_fill_manual(values = c("#DD72A7", "#AA72DD", "#447FBE", "#5FAEE8", "#44BE8A", "#A0BE44"), name = "Dog") +
  scale_size_continuous(range = c(1, 5), name = "Coverage") +
  ggtitle("Distribution of Mapped and Unmapped Reads") +
  theme_bw() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 18),
    axis.title.x = element_text(size = 18),
    axis.title.y = element_text(size = 18),
    axis.text.x = element_text(size = 17),
    legend.title = element_text(size = 15),
    legend.text = element_text(size = 15)
  )

ggsave("/groups/dog/stage/rahma/deepv_cutesv/results/qc_mapping_cov.pdf", plot, width = 12, height = 7)
