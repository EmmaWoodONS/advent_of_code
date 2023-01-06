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
                          "type_score" = c(1:3))

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
  mutate(score = result_score + type_score)

all_games <- data_d2 %>% 
  left_join(combos, by = c("them", "me"))

score <- sum(all_games$score)

