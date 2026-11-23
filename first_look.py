import pandas as pd

df = pd.read_csv("port_calls.csv")

summary = df.groupby(["port", "vessel"])["cost"].sum().reset_index()
summary = summary.sort_values("cost", ascending=False)
total = summary["cost"].sum()
summary["share_%"] = (summary["cost"] / total * 100).round(1)
print(summary)
