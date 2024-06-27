# Python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Local libraries
import procesamiento_datos

def plot_song_by_year():
    df = procesamiento_datos.songs_by_year()
    plt.bar(df['released_year'],df['count'])