import barcode
from barcode.writer import ImageWriter

#define content of the barcode as a string
number = input("Enter the code to generate barcode: ")

#get the required barcode format
barcode_format = barcode.get_barcode_class('upc')

#generate barcode and render as image
my_barcode = barcode_format(number, writer = ImageWriter())

#save barcode as PNG
my_barcode.save("generated_barcode")

from PIL import Image #to open the barcode and visualize
Image.open('generated_barcode.png')

#original source code: clcoding.com
