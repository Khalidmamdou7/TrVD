import pickle
from sklearn.model_selection import train_test_split

# Load dataset
with open("./dataset/dataset.pkl", "rb") as f:
    dataset = pickle.load(f)

# Shuffle dataset if necessary
# Assuming dataset is a list or a pandas DataFrame
# Shuffle if necessary, if not already shuffled

# Split dataset
train_data, temp_data = train_test_split(dataset, test_size=0.2, random_state=42)
val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Save splits
with open("./dataset/trvd_train.pkl", "wb") as f:
    pickle.dump(train_data, f)

with open("./dataset/trvd_val.pkl", "wb") as f:
    pickle.dump(val_data, f)

with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(test_data, f)
