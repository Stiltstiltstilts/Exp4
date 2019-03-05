library(dplyr)
setwd("/Users/courtneyhilton/Research/PhD/Exp4/data/")

trial_data          <- read.delim("001trial_log.txt", sep = "\t", header = TRUE)
trial_data$Sentence <- as.character(trial_data$Sentence)
trial_data$Probe    <- as.character(trial_data$Probe)
trial_data$Accuracy <- as.numeric(trial_data$Accuracy)
trial_data$subnum   <- i
#trial_data$subnum   <- as.factor(trial_data$subnum)
trial_data          <- tbl_df(trial_data)

test <- trial_data %>%
  filter(Sentence_extraction != "assorted", Probe_clause == "main_clause") %>%
  mutate(RT = if_else(RT > 5, true = 5, false = RT)) %>% # replace outliers (RTs > 5sec) with 5sec
  group_by(Congruency, Sentence_extraction) %>%
  summarise(Acc = mean(Accuracy), avg_RT = mean(RT), max_rt = max(RT), min_rt = min(RT))
  

test_relative <- trial_data %>%
  filter(Sentence_extraction != "assorted", Probe_clause == "relative_clause") %>%
  mutate(RT = if_else(RT > 5, true = 5, false = RT)) %>% # replace outliers (RTs > 5sec) with 5sec
  group_by(Congruency, Sentence_extraction) %>%
  summarise(Acc = mean(Accuracy), avg_RT = mean(RT), max_rt = max(RT), min_rt = min(RT))
