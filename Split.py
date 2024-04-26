import pandas as pd
import numpy as np
import os


def split_excel(
    input_excel,
    output_dir,
    train_ratio=0.7,
    val_ratio=0.15,
    test_ratio=0.15,
    random_seed=None,
):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_excel)

    # Shuffle the DataFrame
    if random_seed is not None:
        np.random.seed(random_seed)
    df = df.sample(frac=1).reset_index(drop=True)

    # Calculate the number of rows for each split
    total_rows = len(df)
    train_rows = int(total_rows * train_ratio)
    val_rows = int(total_rows * val_ratio)
    test_rows = total_rows - train_rows - val_rows

    # Split the DataFrame into train, val, and test DataFrames
    train_df = df.iloc[:train_rows]
    val_df = df.iloc[train_rows : train_rows + val_rows]
    test_df = df.iloc[train_rows + val_rows :]

    # Write each split to separate Excel files
    train_file = os.path.join(output_dir, "train.xlsx")
    val_file = os.path.join(output_dir, "val.xlsx")
    test_file = os.path.join(output_dir, "test.xlsx")

    train_df.to_excel(train_file, index=False)
    val_df.to_excel(val_file, index=False)
    test_df.to_excel(test_file, index=False)


if __name__ == "__main__":
    input_excel = "DatasetMadeBySeif.xlsx"  # Change this to your Excel file name
    output_dir = "."  # Change this to the desired output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    split_excel(input_excel, output_dir)
