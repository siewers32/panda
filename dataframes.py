import pandas as pd
import numpy as np

nba = pd.read_csv("nba.csv")
nba["Birthday"] = pd.to_datetime(nba['Birthday'], format = "%m/%d/%y")

# print(nba.sort_values(["Name", "Position"]))
# print(nba.sort_index())
# print(nba.sort_index(axis = "columns"))
# print(nba[["Birthday", "Position"]])
# print(nba.set_index("Name").loc["Kawhi Leonard", ["Team", "Salary"]])
# print(nba)


# nfl = pd.read_csv("nfl.csv")
# nfl["Birthday"] = pd.to_datetime(nfl["Birthday"], format = "%m/%d/%Y")
# nfl.set_index("Name")
# print(nfl[["Name", "Salary"]].sort_values("Salary", ascending = False).head(5))
# print(nfl.sort_values(["Team", "Salary"], ascending = [True, False]))
# nfl.set_index("Birthday")
# print(nfl.reset_index().set_index("Team").loc["New York Jets"].sort_values("Birthday").head(1))


# ==========================================================
#                 Chapter 5
# ==========================================================

emp = pd.read_csv("employees.csv")
emp["Start Date"] = pd.to_datetime(emp['Start Date'], format = "%m/%d/%y")
emp["Mgmt"]= emp["Mgmt"].astype(bool)
emp["Salary"] = emp["Salary"].fillna(0).astype(int)
emp["Gender"] = emp["Gender"].astype("category")
emp["Team"] = emp["Team"].astype("category")
# print(emp.nunique())
allmarias = emp["First Name"] == "Maria"
print(emp[allmarias])


