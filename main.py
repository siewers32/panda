import pandas as pd
import numpy as np

# cols = [1,3] + [i for i in range(7,33)]																												
# students = pd.read_excel("student.xlsx", sheet_name="Cohort 2023", header=3, index_col="Studentnummer", usecols=cols) # 
# movies = pd.read_csv("movies.csv")

# row7 = movies.iloc[200]
# eliminate_nan = (students[] == "nan")
# select = ["3a", 6]
# print(students.columns.values.tolist())
# print(students[select])
# print(students.fillna(""))
# s = pd.Series()
# print(s)
# flavors = [
#     'Chocalte',
#     'Vanilla',
#     'Blueberry',
#     'Strawberry',
#     'Rum raisin',
#     'Pistache',
#     'Hazelnut'
# ]

# f = pd.Series(flavors)
# print(f._data)
# days_of_week = [
#     'monday',
#     'tuesday',
#     'wednesday',
#     'thursday',
#     'friday',
#     'saturday',
#     'sunday'
# ]

# g = pd.Series(flavors, days_of_week)
# print(g)
# print(g.shape)

# lucky_numbers = [
#     4, 8, 16, 32, 64, 128
# ]

# l = pd.Series(lucky_numbers)
# print(l)



# random_data = np.random.randint(1,101,20)
# print(random_data[2])

# values = [i**2 for i in range(0,12)] + [5, 4, 3, 8, np.nan, 9, 11]
# values = [0,1,2,3,4,5,np.nan,6,7,8,11,12,22]
# values = [1,2,3,4]
# nums = pd.Series(data = values)
# # nums = nums + 6
# vals = [i * 3 for i in range(0,6)]
# vals = [2,4,6,8]
# nums2 = pd.Series(vals)
# names = [
#     'Harry',
#     'Klaas',
#     'Bibi'
# ]
# print(list(nums2 + nums))

# superheroes = [
# "Batman",
# "Superman",
# "Spider-Man",
# "Iron Man",
# "Captain America",
# "Wonder Woman"
# ]

# sh = pd.Series(superheroes)
# strength_levels = (100, 120, 90, 95, 110, 120)
# sl = pd.Series(strength_levels)
# tl = pd.Series(data=strength_levels, index=superheroes)
# print(dict(tl * 2))

# ================================================
#                Chapter 3
# ================================================

p = pd.read_csv("pokemon.csv", index_col = "Pokemon").squeeze()
# print(type(p))

g = pd.read_csv('google_stocks.csv', index_col = "Date", parse_dates = ["Date"]).squeeze()
# print(g.describe())
# print(type(g))

rw = pd.read_csv('revolutionary_war.csv', usecols=[ "Start Date", "State"], index_col = "Start Date", parse_dates = ["Start Date"]).squeeze()
print(rw.sort_values(ascending = False))
print(type(rw))
print(p.sort_values(ascending = False))
print(rw.sort_values(na_position = "first"))

