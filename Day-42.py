''' Exercise - 8
               Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
                pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. 
                It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

'''

from pypdf import PdfWriter

merger = PdfWriter()

for pdf in [r"C:\Users\professer_kartik\Desktop\The Ultimate HTML handbook.pdf", r"C:\Users\professer_kartik\Desktop\Git_Handbook.pdf", r"C:\Users\professer_kartik\Desktop\The Ultimate Python Handbook.pdf"]:
    merger.append(pdf)

merger.write("out-basic.pdf")