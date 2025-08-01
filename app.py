import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load clustered data
df = pd.read_csv("clustered_customers.csv")

# Streamlit App Title
st.title("🛍️ E-commerce Customer Segmentation App")

# Sidebar for cluster selection
clusters = sorted(df['cluster'].unique())
selected_cluster = st.sidebar.selectbox("Choose Cluster", clusters)

# Filter by selected cluster
cluster_data = df[df['cluster'] == selected_cluster]

# Show cluster summary
st.header(f"Details for Cluster {selected_cluster}")
st.write(f"**Number of customers in Cluster {selected_cluster}:** {len(cluster_data)}")

# Feature distribution visualization
st.subheader("📊 Cluster Feature Distributions")
selected_features = st.multiselect("Choose features to visualize", df.columns.drop(['user_id', 'cluster']))

# Plot feature distributions
for feature in selected_features:
    fig, ax = plt.subplots()
    ax.hist(cluster_data[feature], bins=20, color='skyblue', edgecolor='black')
    ax.set_title(f"{feature} distribution in Cluster {selected_cluster}")
    st.pyplot(fig)
