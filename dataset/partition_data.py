import pandas as pd
import numpy as np

# Read the Excel file
df = pd.read_excel("DatasetMadeBySeif.xlsx")

# Shuffle the indices to randomize the rows
shuffled_indices = np.random.permutation(df.index)
df_shuffled = df.reindex(shuffled_indices)

# Determine the sizes of train, validation, and test sets
total_size = len(df_shuffled)
train_size = int(0.7 * total_size)
val_size = int(0.15 * total_size)
test_size = total_size - train_size - val_size

# Split the randomized data into train, validation, and test sets
train_df = df_shuffled.iloc[:train_size]
val_df = df_shuffled.iloc[train_size : train_size + val_size]
test_df = df_shuffled.iloc[train_size + val_size :]

# Save the shuffled sets to new Excel files
train_df.to_excel("trvd_train.xlsx", index=False)
val_df.to_excel("trvd_val.xlsx", index=False)
test_df.to_excel("trvd_test.xlsx", index=False)


# Save the sets as pickle files
train_df.to_pickle("trvd_train.pkl")
val_df.to_pickle("trvd_val.pkl")
test_df.to_pickle("trvd_test.pkl")
