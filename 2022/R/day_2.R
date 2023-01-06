# Day 1
# What would your total score be if everything goes exactly according to your strategy guide?
# A x rock 1
# B y paper 2
# C z scissors 3

# Me to win
# A Y
# B Z
# C X
#
# them to win
# A Z
# B X
# C Y

# 0 = loss, 3 = draw, 6 = win

library(dplyr)

data_d2 <- read.csv('2022/data/day_2.csv', header = FALSE) %>% 
  rename(them = V1, 
         me = V2)

type_scores <- data.frame("me" = mine,
                          "t_score" = c(1:3))

theirs <- LETTERS[1:3]
mine <- LETTERS[24:26]
combos <- expand.grid("them" = theirs, "me" = mine) %>% 
  mutate(
    result_score = case_when(
      (them == "A" & me == "Y") | (them == "B" & me == "Z") | (them == "C" & me == "X") ~ 6,
      (them == "A" & me == "X") | (them == "B" & me == "Y") | (them == "C" & me == "Z") ~ 3,
      TRUE ~ 0
  )) %>% 
  left_join(type_scores, by = "me") %>% 
  mutate(score = result_score + t_score)

all_games <- data_d2 %>% 
  left_join(combos, by = c("them", "me"))

score <- sum(all_games$score)

# part 2: 
# X means you need to lose, 
# Y means you need to end the round in a draw, 
# Z means you need to win

# X: 1 for type + 0 for result = 1
# Y: 2 for type + 3 for result = 5
# Z: 3 for type + 6 for result = 9

part_2 <- all_games %>% 
  # mutate(p2_score = ifelse(me == "Y", t_score + 3, 0))
  mutate(
    p2_score = case_when(
      me == "X" ~ as.numeric(t_score),
      me == "Y" ~ as.numeric(t_score) + 3,
      me == "Z" ~ as.numeric(t_score) + 6
    )) 

part_2_score <- sum(part_2$p2_score)

