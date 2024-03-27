import pandas as pd

df = pd.read_pickle("your_file.pkl")


df.to_excel("output.xlsx", index=False)
