from PIL import Image

def Images_Pdf(filename, output):
    images = []
    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)
        images[0].save(output, save_all = True, append_images = images[1:])

#import images, export PDF
Images_Pdf(["flowers_1.jpg", "flowers_2.jpg", "flowers_3.jpg", "flowers_4.jpg", "flowers_5.jpg"], "Images_PDF.pdf")

#free stock photos from pexels.com
#code inspired by clcoding.com
