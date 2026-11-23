import pandas as pd

# Load the data
df = pd.read_csv("port_calls.csv")

# Step 23: total cost per port + vessel, sorted highest first
summary = df.groupby(["port", "vessel"])["cost"].sum().reset_index()
summary = summary.sort_values("cost", ascending=False)
# print(summary)

# Step 24: top 3 most expensive combinations
top3 = summary.head(3)
# print(top3)

# Step 25: each row's share of total cost, as a %
total = summary["cost"].sum()
summary["share_%"] = (summary["cost"] / total * 100).round(1)
# print(summary)

# Step 27: save the summary to a CSV file
summary.to_csv("cost_summary.csv", index=False)

# Step 28: several numbers per port at once
port_stats = df.groupby("port")["cost"].agg(["sum", "mean", "count", "max", "min"]).reset_index()
# print(port_stats)

# Step 30: ports with average cost above 12,000
# expensive = port_stats[(port_stats["mean"] > 12000) & (port_stats["count"]>=3)]
# print(expensive)
# Step 31: Your turn to write it shows only the ports with more than 1 call.
# Step 33: monthly cost per port, like an Excel pivot
# pivot = df.pivot_table(index="port", columns="month", values="cost", aggfunc="sum", fill_value=0)
# print(pivot)

vessel_spend = df.groupby("vessel")["cost"].sum(). sort_values(ascending=False)
print(vessel_spend)
