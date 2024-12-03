# Kyle Pendleton
# 02/12/2024
# this will extract images from the specified PDF file

#!usr/bin/env python3

import pymupdf

document = pymupdf.open("PDF/10-page-sample.pdf")
for current_page in range(len(document)):
    for image in document.get_page_images(current_page):
        xref = image[0]
        pix = pymupdf.Pixmap(document, xref)
        pix.save("page%s-%s.png" % (current_page, xref))
        print("Extracted image page%s-%s.png" % (current_page, xref))