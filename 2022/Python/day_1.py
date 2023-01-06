import pandas as pd
import numpy as np
from numpy import NaN as nan
from itertools import groupby

data_d1 = pd.read_csv('data/day_1.csv', header = None)
calories = np.array(data_d1[0])

by_elf = [np.sum(list(v)) for k, v in groupby(calories, np.isfinite) if k]

max_calories = max(by_elf)

# part 2: top 3 elves
top_3_sum = np.sum(sorted(by_elf, reverse = True)[0:3])
