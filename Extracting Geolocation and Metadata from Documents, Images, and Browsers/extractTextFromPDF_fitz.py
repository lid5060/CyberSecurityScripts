# Kyle Pendleton
# 02/12/2024
# this programme will extract text from a specified PDF file

#!usr/bin/env python3

import fitz

pdf_file = "PDF/10-page-sample.pdf"
document = fitz.open(pdf_file)
print ("number of pages: %i" % document.page_count)

page_number_input= input("Enter page number:")

page = document.load_page(int(page_number_input)-1)
extracted_page_data = page.get_text("text")
print(extracted_page_data)