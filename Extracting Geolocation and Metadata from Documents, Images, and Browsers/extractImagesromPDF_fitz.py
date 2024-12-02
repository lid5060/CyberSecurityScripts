# Kyle Pendleton
# 02/12/2024
# this script will extract images from a pdf file

#!usr/bin/env python3

import fitz

document = fitz.open("PDF/10-page-sample.pdf")
for users_current_page in range(len(document)):
    for image in document.get_page_images(users_current_page):
        xref = image[0]
        pix = fitz.Pixmap(document, xref)
        pix.save("page%s-%s.png" % (users_current_page, xref))
        print("Extracted image page%s-%s.png" % (users_current_page, xref))