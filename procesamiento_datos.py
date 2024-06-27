import pandas as pd

def load_data():
    path_data = "C:/Users/HerbertRaulLizamaBas/OneDrive - MACROPAY/Documentos/Personal/Repositories/Genera reporte PDF/data/spotify-2023.csv"
    return pd.read_csv(path_data,encoding='latin-1')

def songs_by_year():
    df = load_data()
    return pd.DataFrame(df['released_year'].value_counts().reset_index())