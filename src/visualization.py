import matplotlib.pyplot as plt

def plot_trends(df):
    plt.figure()
    plt.plot(df['date'], df['temperature'])
    plt.title("Temperature Over Time")
    plt.savefig("outputs/plots/time_series.png")
    plt.close()