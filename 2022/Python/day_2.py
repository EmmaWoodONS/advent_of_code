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
data_d2.columns = ["theirs", "mine"]

combos = np.array([(x, y) for x in ("A", "B", "C") for y in (["X", 1], ["Y", 2], ["Z", 3])], dtype = "object")
combos_df = pd.DataFrame(combos, columns = ['them','me'])
type_scores = pd.DataFrame(combos_df['me'].tolist(),\
     columns = ['me', 'type_score']).join(combos_df["them"])

win = pd.DataFrame(np.array([["A", "Y", 6], ["B", "Z", 6], ["C", "X", 6]]), columns = ["them", "me", "result_score"])
lose = pd.DataFrame(np.array([["A", "Z", 0], ["B", "X", 0], ["C", "Y", 0]]), columns = ["them", "me", "result_score"])
draw = pd.DataFrame(np.array([["A", "X", 3], ["B", "Y", 3], ["C", "Z", 3]]), columns = ["them", "me", "result_score"])
result_scores = pd.concat([win, lose, draw])

scores_joined = type_scores.merge(result_scores) 
