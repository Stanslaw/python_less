import pandas as pd

ship = pd.read_csv("titanic.csv")
# print(ship)
#
# print(ship.shape)
# print(ship.dtypes)

my_data = pd.DataFrame([['A', 10], ['A', 14], ['B', 12], ['B', 23]], columns=['type', 'value'])

print(my_data)
print(my_data.type)



