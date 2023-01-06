# Me to win
# A Y
# B Z
# C X
#
# them to win
# A Z
# B X
# C Y

import pandas as pd
import numpy as np

data_d2 = pd.read_csv('data/day_2.csv', header = None)
data_d2.columns = ["them", "me"]

combos = np.array([(x, y) for x in ("A", "B", "C") for y in (["X", 1], ["Y", 2], ["Z", 3])], dtype = "object")
combos_df = pd.DataFrame(combos, columns = ["them", "me"])
type_scores = pd.DataFrame(combos_df["me"].tolist(),\
     columns = ["me", "type_score"]).join(combos_df["them"])

win = pd.DataFrame(np.array([["A", "Y", 6], ["B", "Z", 6], ["C", "X", 6]]), columns = ["them", "me", "result_score"])
lose = pd.DataFrame(np.array([["A", "Z", 0], ["B", "X", 0], ["C", "Y", 0]]), columns = ["them", "me", "result_score"])
draw = pd.DataFrame(np.array([["A", "X", 3], ["B", "Y", 3], ["C", "Z", 3]]), columns = ["them", "me", "result_score"])
result_scores = pd.concat([win, lose, draw])

scores_joined = type_scores.merge(result_scores).merge(data_d2) 
scores_joined["final_score"] = pd.to_numeric(scores_joined["result_score"]) + pd.to_numeric(scores_joined["type_score"])

score = scores_joined["final_score"].sum()

# part 2: 
# X means you need to lose, 
# Y means you need to end the round in a draw, 
# Z means you need to win

# X: 1 for type + 0 for result = 1
# Y: 2 for type + 3 for result = 5
# Z: 3 for type + 6 for result = 9
p2_scores = scores_joined.copy().loc[:, ["them", "me", "type_score"]]
p2_scores["type_score"] = p2_scores["type_score"].replace([2, 3], [5, 9])
p2_final_score = p2_scores["type_score"].sum()