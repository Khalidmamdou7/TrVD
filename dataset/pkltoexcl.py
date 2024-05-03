import pandas as pd
import pickle


def pickle_to_excel(pickle_file, excel_file):
    try:
        # Load data from pickle file
        with open(pickle_file, "rb") as f:
            data = pickle.load(f)

        # Extract labels and codes from the data
        labels = [item["label"] for item in data]
        codes = [item["code"] for item in data]

        # Create a DataFrame with "label" and "code" columns
        df = pd.DataFrame({"label": labels, "code": codes})

        # Save DataFrame to Excel file
        df.to_excel(excel_file, index=False)

        print("Data saved to Excel file successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


# Usage example
pickle_to_excel("dataset.pkl", "dataset.xlsx")
