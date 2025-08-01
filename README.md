#  Ecommerce Customer Clustering (Streamlit App)

This project uses unsupervised learning to cluster e-commerce customers based on their shopping behavior. A Streamlit dashboard is built to visualize clusters and provide insights for marketing.

## folder structure
Ecommerce_Customer_Segmentation/
│
├── app.py                       # Streamlit app to display clusters & insights
├── main.py                      # Main Python script for data processing & clustering
├── requirements.txt             # All required Python packages
├── clustering.py                    
├── insights.py                  
│
├── data/                        # Raw and processed data files
│   ├── Ecommerce_data.db        # Original SQLite database
│   └── ecommerce_cleaned.csv    # Cleaned version if extracted from DB
│
├── outputs/                     # All output files
│   └── clustered_customers.csv  # Final output with cluster labels
│
├──processing.py                      
│   
│
│
└── venv/                        # Your Python virtual environment (do NOT zip this)



## Features
- Data preprocessing and feature engineering
- KMeans clustering with Elbow Method
- Clustered user segmentation (low/high spenders, active buyers, etc.)
- Streamlit-based interactive dashboard
- Exported `clustered_customers.csv` with cluster labels

## Tech Stack
- Python, Pandas, Scikit-Learn
- Streamlit
- Matplotlib / Seaborn (optional for visualization)
- Git/GitHub

##  How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

# Model Deployement
Ecommerce_Customer_Segmentation/
│
├── app.py                      # ✅ Streamlit app (main interface)
├── requirements.txt            # ✅ All required packages
│
├── outputs/
│   └── clustered_customers.csv # ✅ Your clustered output data
│
├── data/
│   └── Ecommerce_data.db       # (Optional) Your source database if needed
