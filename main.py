from fpdf import FPDF
import pandas as pd 

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=12)
    #font size and line are recommeneded to be the same for better readability

    pdf.set_text_color(254, 0, 0)

    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align='L')
    # w: width of the cell, h: height of the cell, txt: text to be printed, ln: whether to move to the next line after printing, align: alignment of the text, border: whether to draw a border around the cell

    pdf.line(x1=10, y1=20, x2=200, y2=20 )

pdf.output('output.pdf')

