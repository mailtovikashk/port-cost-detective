#when filtering rows for example

take a variable name and equate it to the logic
example
first read the csv by
df=pd.read_csv("port_calls.csv")

and then variable

jebel_ali = df[df["port"] == "Jebel Ali"]
print(jebel_ali)#

more----****
   filter rows:  df[df["port"] == "Jebel Ali"]
   sum a column: df["cost"].sum()
   group:        df.groupby("month")["cost"].sum()