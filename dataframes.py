import pandas as pd
import numpy as np

nba = pd.read_csv("nba.csv")
# nba["Birthday"] = pd.to_datetime(nba['Birthday'], format = "mm/dd/YY")
print(nba)