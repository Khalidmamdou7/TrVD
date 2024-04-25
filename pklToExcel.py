import pandas as pd

df = pd.read_pickle("./dataset/trvd_test.pkl")


df.to_excel("output.xlsx", index=False)
