# Python libraries
from fpdf import FPDF

# Local libraries
import grafica

# Dimensiones en mm de la pagina
WIDTH = 210
HEIGHT = 297

# Primera pagina
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)
pdf.cell(40,10,'Hello world!')

# Barplot streams by year
grafica.plot_streams_by_year()
pdf.image('stream_by_year_realease.png',0,30,WIDTH/2)

# Barplot streams by month
grafica.plot_streams_by_month()
pdf.image('stream_by_month_realease.png',WIDTH/2,30,WIDTH/2)

# Guardamos PDF
pdf.output('tutorial.pdf','F')