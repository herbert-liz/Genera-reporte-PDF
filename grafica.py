# Python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Local libraries
import procesamiento_datos

# Plot total streams by year of release
def plot_streams_by_year():
    df = procesamiento_datos.streams_by_year()
    plt.bar(df['released_year'],df['streams'])
    plt.savefig('stream_by_year_realease.png')
    print("Plot saved as 'stream_by_year_realease.png'")
    plt.close()

# Plot total streams by month of release
def plot_streams_by_month():
    df = procesamiento_datos.streams_by_month()
    plt.bar(df['released_month'],df['streams'])
    plt.savefig('stream_by_month_realease.png')
    print("Plot saved as 'stream_by_month_realease.png'")
    plt.close()