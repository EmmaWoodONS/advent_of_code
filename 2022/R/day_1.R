# Day 1
# How many Calories are being carried by the Elf carrying the most Calories?
library(dplyr)

data_d1 <- read.csv('2022/data/day_1.csv', header = FALSE) 

data_by_elf <- data_d1 %>% 
  rename(calories = V1) %>% 
  mutate(elf = row_number()) %>% 
  mutate(elf = ifelse((is.na(calories)|elf == 1), as.character(elf), NA)) %>% 
  fill(elf) %>% 
  filter(!is.na(calories)) 

totals <- data_by_elf %>% 
  group_by(elf) %>%
  summarise(total_calories = sum(calories))
  
most = max(totals$total_calories)

