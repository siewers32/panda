import pandas as pd
import numpy as np

cols = [1,3] + [i for i in range(7,33)]																												
students = pd.read_excel("student.xlsx", sheet_name="Cohort 2023", header=3, index_col="Studentnummer", usecols=cols) # 
# movies = pd.read_csv("movies.csv")

# row7 = movies.iloc[200]
# eliminate_nan = (students[] == "nan")
select = ["3a", 6]
print(students.columns.values.tolist())
# print(students[select])
print(students.fillna(""))