from fpdf import FPDF
import pandas as pd 

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0) # disable automatic page break and set margin to 0 to have more control over the layout of the pages

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    #header

    pdf.set_font(family='Times', style='B', size=12)
    #font size and line are recommeneded to be the same for better readability

    pdf.set_text_color(100, 100, 100) # RGB color for the text:grey

    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1, align='L')
    # w: width of the cell, h: height of the cell, txt: text to be printed, ln: whether to move to the next line after printing, align: alignment of the text, border: whether to draw a border around the cell

    #lines
    for y in range(20, 277, 10):
        pdf.line(10,y,200,y) # x1, y1, x2, y2 coordinates of the line

    #for the footer

    pdf.ln(265) # move the cursor to the bottom of the page
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(150, 150, 150) # RGB color for the text: light grey
    pdf.cell(w=0, h=10, txt=row['Topic'], ln=1, align='R')

    for i in range(row["Pages"]-1):
        pdf.add_page()

        pdf.ln(277) # move the cursor to the bottom of the page
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(150, 150, 150) # RGB color for the text: light grey
        pdf.cell(w=0, h=10, txt=row['Topic'], ln=1, align='R')
        
        for y in range(20, 277, 10):
            pdf.line(10,y,200,y) # x1, y1, x2, y2 coordinates of the line

pdf.output('output.pdf')

