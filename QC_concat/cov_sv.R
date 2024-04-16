library(ggplot2)

data <- read.csv(file = "/groups/dog/stage/rahma/deepv_cutesv/cov_sv.csv")

plot <- ggplot(data, aes(x = Sample, y = CuteSV, fill = Coverage)) +
  geom_bar(stat = "identity") +
  labs(x = "Samples", y = "Structural variants", fill = "Sample Coverage") +
  ggtitle("Number of Structural Variants (by cuteSV) per Sample") + theme_bw() +
  scale_fill_distiller(palette = "Blues", direction = 1) +
  theme(
    plot.title = element_text(hjust = 0.5, size = 18),
    axis.title.x = element_text(size = 18),
    axis.title.y = element_text(size = 18),
    axis.text.x = element_text(size = 17),
  )

ggsave("/groups/dog/stage/rahma/deepv_cutesv/results/cov_sv.pdf", plot, width = 12, height = 7)
