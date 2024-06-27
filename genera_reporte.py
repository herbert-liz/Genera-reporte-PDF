# Python libraries
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime, timedelta
import os

# Local libraries
import procesamiento_datos
import grafica

grafica.plot_song_by_year()
plt.show()