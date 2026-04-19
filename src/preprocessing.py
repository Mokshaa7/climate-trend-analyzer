import pandas as pd
def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    
    df = df.fillna(method='ffill')
    
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    return df