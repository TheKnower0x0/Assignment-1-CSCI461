import pandas as pd
import os
import argparse
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


def clean_data(df):
    """Clean the data by filling missing values and removing duplicates."""
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Annual Income (k$)'] = df['Annual Income (k$)'].fillna(
        df['Annual Income (k$)'].median())
    df['Spending Score (1-100)'] = df['Spending Score (1-100)'].fillna(
        df['Spending Score (1-100)'].median())
    df = df.drop_duplicates()
    return df


def transform_data(df):
    """Transform data by encoding categorical variables and scaling features."""
    df['Genre'] = df['Genre'].map({'Male': 1, 'Female': 0})
    scaler = MinMaxScaler()
    df[['Annual Income (k$)', 'Spending Score (1-100)']] = scaler.fit_transform(
        df[['Annual Income (k$)', 'Spending Score (1-100)']]
    )
    return df


def reduce_data(df):
    """Reduce dimensionality of data using PCA."""
    pca = PCA(n_components=2)
    components = pca.fit_transform(
        df[['Annual Income (k$)', 'Spending Score (1-100)']])
    df['PCA1'] = components[:, 0]
    df['PCA2'] = components[:, 1]
    return df


def discretize_data(df):
    """Create Income Level column by binning Annual Income."""
    df['Income_Level'] = pd.qcut(df['Annual Income (k$)'], q=4, labels=[
                                 'Low', 'Medium', 'High', 'Very High'])
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform data preprocessing.")
    parser.add_argument('input_path', type=str,
                        help="Path to the input dataset file.")
    parser.add_argument('output_path', type=str, nargs='?', default=os.path.join(os.getcwd(), 'service-result', 'res_dpre.csv'),
                        help="Path to save the preprocessed dataset.")
    args = parser.parse_args()

    # Load the dataset
    try:
        df = pd.read_csv(args.input_path)
    except FileNotFoundError:
        print(f"File not found: {args.input_path}")
        exit(1)

    # Clean, transform, reduce, and discretize the dataset
    df = clean_data(df)
    df = transform_data(df)
    df = reduce_data(df)
    df = discretize_data(df)

    # Save the processed dataset
    output_dir = os.path.dirname(args.output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Check if directory creation was successful
    if not os.path.exists(output_dir):
        print(f"Failed to create directory: {output_dir}")
        exit(1)

    df.to_csv(args.output_path, index=False)
    print(f"Preprocessed dataset saved to {args.output_path}")
