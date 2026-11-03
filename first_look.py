import pandas as pd
df = pd.read_csv("port_calls.csv")
df["cost_usd"]=df["cost"]/3.6725
df["cost_usd"]=df["cost_usd"].round(2)
print(df)
