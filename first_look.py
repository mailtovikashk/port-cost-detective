import pandas as pd

df = pd.read_csv("port_calls.csv")

result = df.groupby("vessel")["cost"].mean().sort_values(ascending=False)
print(result)