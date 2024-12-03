# Kyle Pendleton
# 02/12/2024
# this will extract data from the specified PDF file

#!usr/bin/env python3

import PyPDF2

pdf_file = open("PDF/10-page-sample.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdf_file)

page_numbers = input("Enter page number:")
page_object = pdfReader.getPage(int(page_numbers)-1)
pdf_text = str(page_object.extractText())

print(pdf_text)