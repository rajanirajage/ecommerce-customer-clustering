# insights.py
import pandas as pd

def generate_cluster_insights(df, cluster_column='cluster'):
    insights = []

    grouped = df.groupby(cluster_column)
    for cluster_id, group in grouped:
        info = {
            'Cluster': cluster_id,
            'Users': group['user_id'].nunique(),
            'Most_Viewed_Category': group['category_code'].mode()[0] if not group['category_code'].isna().all() else 'Unknown',
            'Avg_Price': round(group['price'].mean(), 2),
            'Most_Common_Event': group['event_type'].mode()[0]
        }
        insights.append(info)

    return pd.DataFrame(insights)
