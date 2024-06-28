# Python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Local libraries
import procesamiento_datos

# Crea la grafica
def plot_song_by_year():
    df = procesamiento_datos.songs_by_year()
    plt.bar(df['released_year'],df['count'])
    plt.savefig('song_by_year.png')
    print("Plot saved as 'songs_by_year.png'")
    plt.close()