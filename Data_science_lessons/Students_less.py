import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")

print(data[-10:])

print(data.shape[0])

print(data[data["lunch"] == "free/reduced"].shape[0])

print(round(data[data["lunch"] == "free/reduced"].shape[0] / data.shape[0], 10))