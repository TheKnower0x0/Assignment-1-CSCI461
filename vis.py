import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os


def create_visualization(df, output_path):
    if 'Income_Level' not in df.columns:
        print("Income_Level column not found in the dataset. Cannot create visualization.")
        return

    avg_spending_by_income = df.groupby(
        'Income_Level')['Spending Score (1-100)'].mean()
    plt.figure(figsize=(10, 6))
    avg_spending_by_income.plot(kind='bar')
    plt.title("Average Spending Score by Income Level")
    plt.xlabel("Income Level")
    plt.ylabel("Average Spending Score (1-100)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create data visualization.")
    parser.add_argument('input_path', type=str,
                        help="Path to the input dataset file.")
    parser.add_argument('output_path', type=str, nargs='?', default=os.path.join(os.getcwd(), 'service-result', 'vis.png'),
                        help="Path to save the visualization.")
    args = parser.parse_args()

    # Load the dataset
    df = pd.read_csv(args.input_path)

    # Create and save the visualization
    create_visualization(df, args.output_path)
    print(f"Visualization saved to {args.output_path}")
