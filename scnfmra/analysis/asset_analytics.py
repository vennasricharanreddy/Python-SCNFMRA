import pandas as pd

def asset_health(data):
    df = pd.DataFrame(data)
    return df["health_status"].value_counts()