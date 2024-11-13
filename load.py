import argparse
import pandas as pd
import os


def read_dataset(file_path):
    """
    Reads a dataset from the given file path.
    The function assumes the file is in CSV format.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"An error occurred while reading the dataset: {e}")
        return None


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser(description="Read a dataset file.")

    # Adding required argument
    parser.add_argument('file_path', type=str, nargs='?', default=os.path.join(os.getcwd(), "Mall_Customers.csv"),
                        help="Path to the dataset file.")

    # Parse the argument
    args = parser.parse_args()

    # Read the dataset
    dataset = read_dataset(args.file_path)

    if dataset is not None:
        print("Dataset loaded successfully!")
        print(dataset.head())  # Display the first few rows of the dataset
    else:
        print("Failed to load the dataset.")
