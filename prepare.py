import pickle
import pandas as pd


df = pd.read_excel("DatasetMadeBySeif.xlsx", usecols=["label", "code"])

with open("./dataset/dataset.pkl", "wb") as f:
    pickle.dump(df, f)
