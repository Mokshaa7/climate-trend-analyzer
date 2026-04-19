from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.analysis import trend_analysis
from src.anomaly import detect_anomalies
from src.forecasting import forecast_temperature
from src.visualization import plot_trends

def main():
    df = load_data("data/raw/climate_data.csv")
    
    df = preprocess_data(df)
    
    trend_analysis(df)
    
    df = detect_anomalies(df)
    
    forecast_temperature(df)
    
    plot_trends(df)

if __name__ == "__main__":
    main()