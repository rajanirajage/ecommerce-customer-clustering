import os
from preprocessing import load_and_process_data
from clustering import perform_kmeans_clustering
import pandas as pd

def main():
    print("🔄 Loading and processing data...")
    features_df = load_and_process_data('data/Database.db')

    print("📊 Performing KMeans clustering...")
    clustered_df, model = perform_kmeans_clustering(features_df)

    # Ensure outputs directory exists
    os.makedirs('outputs', exist_ok=True)

    # Save clustered customer data
    output_path = os.path.join('outputs', 'clustered_customers.csv')
    clustered_df.to_csv(output_path, index=False)
    print(f"✅ Clustered customer data saved to {output_path}")

if __name__ == "__main__":
    main()
