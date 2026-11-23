import pandas as pd

df = pd.read_csv("port_calls.csv")

summary = df.groupby(["port", "vessel"])["cost"].sum().reset_index()
summary = summary.sort_values("cost", ascending=False)
print(summary)
