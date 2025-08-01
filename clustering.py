import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def perform_kmeans_clustering(data, max_k=10):
    """Performs KMeans clustering and returns clustered data and model."""
    os.makedirs("outputs", exist_ok=True)  # Ensure the outputs/ folder exists

    wcss = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)

    # Plot the elbow graph
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_k + 1), wcss, marker='o')
    plt.title('Elbow Method for Optimal Clusters')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/elbow_plot.png")
    plt.close()

    # Use optimal k (you can manually decide or automate with elbow point)
    optimal_k = 4  # You can change this after inspecting elbow_plot.png
    final_kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
    cluster_labels = final_kmeans.fit_predict(data)

    # Append cluster labels to original data
    clustered_df = data.copy()
    clustered_df['Cluster'] = cluster_labels

    # Save to CSV
    clustered_df.to_csv("outputs/clustered_customers.csv", index=False)

    return clustered_df, final_kmeans
