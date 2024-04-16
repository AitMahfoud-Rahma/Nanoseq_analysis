library(ggplot2)
data <- read.csv("/groups/dog/stage/rahma/deepv_cutesv/results/variant_calling/sniffles/sv_types.csv")

grouped_data <- aggregate(Count ~ File + Variant.Type, data = data, sum)

plot <- ggplot(grouped_data, aes(x = File, y = Count, fill = Variant.Type)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Counts of Variant Types by sample", x = "Samples", y = "Number of variants") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 14),  #la taille de la police des axes x
        axis.text.y = element_text(size = 14),  # la taille de la police des axes y
        plot.title = element_text(size = 24, hjust = 0.5),  # le titre 
        axis.title.x = element_text(size = 14),  # la taille de la police de l'axe x
        axis.title.y = element_text(size = 14)) +  #la taille de la police de l'axe y
  scale_fill_brewer(palette = "Paired") +
  guides(fill = guide_legend(title = "Variant Type"))

ggsave("sv_types_grouped_bar.png", plot, width = 12, height = 7)
