import pandas as pd
from sklearn.model_selection import train_test_split
import pickle


def read_data_from_source(file_path):
    data = pd.read_excel(file_path)
    return data


data = read_data_from_source("DatasetMadeBySeif.xlsx")

# Splitting the data into features (X) and labels (y)
X = data.drop(columns=["label", "code"])
y = data["code"]

# Splitting the entire dataset into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.1765, random_state=42
)  # 0.15 / (1 - 0.15)

# Save the split datasets into pickle files
with open("./dataset/trvd_train.pkl", "wb") as f:
    pickle.dump((X_train, y_train), f)

with open("./dataset/trvd_val.pkl", "wb") as f:
    pickle.dump((X_val, y_val), f)

with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump((X_test, y_test), f)
