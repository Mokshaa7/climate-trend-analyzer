import pandas as pd
import numpy as np

dates = pd.date_range(start="2010-01-01", periods=3650)

data = pd.DataFrame({
    "date": dates,
    "temperature": 25 + np.sin(np.arange(3650)/365)*10 + np.random.normal(0,2,3650),
    "rainfall": np.random.gamma(2,2,3650),
    "humidity": np.random.uniform(40,90,3650)
})

data.to_csv("data/raw/climate_data.csv", index=False)