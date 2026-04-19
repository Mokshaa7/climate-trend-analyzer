import matplotlib.pyplot as plt

def trend_analysis(df):
    df.groupby('year')['temperature'].mean().plot()
    plt.title("Yearly Temperature Trend")
    plt.savefig("outputs/plots/temp_trend.png")
    plt.close()