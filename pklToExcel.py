import pandas as pd

df = pd.read_pickle("./dataset/dataset.pkl")


df.to_excel("output.xlsx", index=False)
