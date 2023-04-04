#pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import _baseFontName, _baseFontNameB

#create new PDF file
pdf = canvas.Canvas('PDF_python_generated_01.pdf', pagesize=A4)

#adding text inside
PAGE_HEIGHT = pdf._pagesize[1]
pdf.setStrokeColor(red)
pdf.setFont('Helvetica',12)
pdf.drawString(72, 720, 'Lorem Ipsum')
pdf.drawString(72, 700, 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet.')
pdf.drawString(72, 680, 'Nor is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain')
pdf.drawString(72, 660, 'Fillerama')
pdf.drawString(72, 640, 'DeLorean Ipsum')
pdf.setLineWidth(0.5)
pdf.line(66,00,66,PAGE_HEIGHT-72)
pdf.line(00,750,580,750) 


#saving the PDF
pdf.save()

#code inspired by clcoding.com and programcreek.com
