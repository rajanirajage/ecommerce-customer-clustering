#  Ecommerce Customer Clustering (Streamlit App)

This project uses unsupervised learning to cluster e-commerce customers based on their shopping behavior. A Streamlit dashboard is built to visualize clusters and provide insights for marketing.

## folder structure
Ecommerce_Customer_Segmentation/
│
├── app.py                        
├── main.py                     
├── requirements.txt           
├── clustering.py                    
├── insights.py                  
├── data/                       
│   ├── Ecommerce_data.db      
│   └── ecommerce_cleaned.csv 
├── outputs/                   
│   └── clustered_customers.csv  
├──processing.py                      



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
