import pandas as pd

d1 = pd.read_csv('dataset1.csv')
print(d1.head())

# print(d1["Menu Name"])

# print(d1.loc['Menu Name'])

print(d1.iloc[1,:])