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
#from numpy import NaN as nan
#from itertools import groupby

data_d2 = pd.read_csv('data/day_2.csv', header = None)
data_d2.columns = ["theirs", "mine"]

combos = np.array([(x, y) for x in ("A", "B", "C") for y in ("X", "Y", "Z")])


#win = np.array([["A", "Y"], ["B", "Z"], ["C", "X"]])
#lose = np.array([["A", "Z"], ["B", "X"], ["C", "Y"]])
#draw = np.array([["A", "X"], ["B", "Y"], ["C", "Z"]])
