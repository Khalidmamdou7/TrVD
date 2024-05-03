import pandas as pd
import pickle


def pickle_to_excel(pickle_file, excel_file):
    try:
        # Load data from pickle file
        with open(pickle_file, "rb") as f:
            data = pickle.load(f)

        print("Data loaded successfully from pickle file.")
        print("Type of loaded data:", type(data))
        print("Loaded data:", data)

        # Ensure that the loaded data is a list
        if not isinstance(data, list):
            raise ValueError(
                "Data in pickle file is not in the expected format (list of dictionaries)."
            )

        # Extract labels and codes from the data
        labels = [item.get("label") for item in data]
        codes = [item.get("code") for item in data]

        print("Labels and codes extracted successfully.")

        # Create a DataFrame with "label" and "code" columns
        df = pd.DataFrame({"label": labels, "code": codes})

        # Save DataFrame to Excel file
        df.to_excel(excel_file, index=False)

        print("Data saved to Excel file successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


# Usage example
pickle_to_excel("train.pkl", "train.xlsx")
