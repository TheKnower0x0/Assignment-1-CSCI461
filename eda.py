import pandas as pd
import argparse
import os


def generate_insights(df):
    insights = [
        f"Average Age: {df['Age'].mean()}",
        f"Gender Distribution: {df['Genre'].value_counts().to_dict()}",
        f"Spending Score Range: {
            df['Spending Score (1-100)'].min()} - {df['Spending Score (1-100)'].max()}",
        f"Average Annual Income: {df['Annual Income (k$)'].mean()}",
        f"Customer Count by Income Level: {df['Income_Level'].value_counts().to_dict(
        ) if 'Income_Level' in df.columns else 'Income_Level not available'}"
    ]
    return insights


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Perform exploratory data analysis.")
    parser.add_argument('input_path', type=str,
                        help="Path to the input dataset file.")
    parser.add_argument('output_dir', type=str, nargs='?', default=os.path.join(os.getcwd(), 'service-result'),
                        help="Directory to save the insights.")
    args = parser.parse_args()

    # Load the dataset
    df = pd.read_csv(args.input_path)

    # Generate insights
    insights = generate_insights(df)

    # Ensure output directory exists
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # Save insights to text files
    for idx, insight in enumerate(insights, start=1):
        output_path = os.path.join(args.output_dir, f'eda-in-{idx}.txt')
        with open(output_path, 'w') as f:
            f.write(insight)
    print(f"EDA insights saved to {args.output_dir}")
