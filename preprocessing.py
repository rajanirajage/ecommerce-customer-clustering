import pandas as pd
import sqlite3
from sklearn.preprocessing import LabelEncoder

def load_and_process_data(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM Ecommerce_data", conn)
    conn.close()

    df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')
    df = df.dropna(subset=['event_time', 'event_type', 'product_id', 'price', 'user_id']).drop_duplicates()

    for col in ['category_id', 'category_code', 'brand', 'user_session']:
        df[col] = df[col].fillna('unknown')

    df['event_type_encoded'] = LabelEncoder().fit_transform(df['event_type'])
    df['brand_encoded'] = LabelEncoder().fit_transform(df['brand'])
    df['category_code_encoded'] = LabelEncoder().fit_transform(df['category_code'])

    agg_df = df.groupby('user_id').agg({
        'event_type_encoded': 'mean',
        'brand_encoded': 'nunique',
        'category_code_encoded': 'nunique',
        'price': ['mean', 'max'],
        'product_id': 'nunique',
        'user_session': 'nunique'
    }).reset_index()

    agg_df.columns = ['user_id', 'avg_event_type', 'unique_brands', 'unique_categories',
                      'avg_price', 'max_price', 'unique_products', 'unique_sessions']
    
    return agg_df
