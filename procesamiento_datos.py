import pandas as pd

def load_data():
    path_data = "./data/spotify-2023.csv"
    return pd.read_csv(path_data,encoding='latin-1')

# Total streams by year
def streams_by_year():
    df = load_data()
    df['streams'] = pd.to_numeric(df['streams'],errors='coerce')
    return pd.DataFrame(df.groupby('released_year')['streams'].sum().reset_index())

# Total streams by month
def streams_by_month():
    df = load_data()
    df['streams'] = pd.to_numeric(df['streams'],errors='coerce')
    return pd.DataFrame(df.groupby('released_month')['streams'].sum().reset_index())