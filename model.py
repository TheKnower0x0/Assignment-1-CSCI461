import pandas as pd
from sklearn.cluster import KMeans
import argparse
import os


def perform_kmeans(df, n_clusters=3):
    features = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(features)
    return cluster_labels


def save_cluster_counts(cluster_labels, output_path):
    cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()
    with open(output_path, 'w') as file:
        for cluster, count in cluster_counts.items():
            file.write(f"Cluster {cluster}: {count} records\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform K-means clustering.")
    parser.add_argument('input_path', type=str,
                        help="Path to the input dataset file.")
    parser.add_argument('output_path', type=str, nargs='?', default=os.path.join(os.getcwd(), 'service-result', 'k.txt'),
                        help="Path to save the cluster counts.")
    args = parser.parse_args()

    # Load the dataset
    df = pd.read_csv(args.input_path)

    # Perform K-means clustering
    cluster_labels = perform_kmeans(df)

    # Save the count of records in each cluster
    save_cluster_counts(cluster_labels, args.output_path)
    print(f"Cluster information saved to {args.output_path}")
