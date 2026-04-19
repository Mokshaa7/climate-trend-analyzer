from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_temperature(df):
    df['time_index'] = np.arange(len(df))
    
    X = df[['time_index']]
    y = df['temperature']
    
    model = LinearRegression()
    model.fit(X, y)
    
    future = np.array([[len(df) + i] for i in range(30)])
    preds = model.predict(future)
    
    print("Forecast completed")