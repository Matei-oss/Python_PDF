#PYTHON PDF's

import PyPDF2 
import sys 

# rb - read binary
inputs = sys.argv[1:]

pdf_list = ['dummy.pdf','twopage.pdf','wtr.pdf']

def pdf_combiner(pdf_list):
   merger = PyPDF2.PdfFileMerger()
   for pdf in pdf_list:
     print(pdf)
     merger.append(pdf)
   merger.write('merged.pdf')
  

 pdf_combiner(pdf_list)

 with open('dummy.pdf','rb') as file:
   reader = PyPDF2.PdfFileReader(file)
   print(f' The file has {reader.numPages} page(s).')

 with open('twopage.pdf','rb') as file2:
   reader = PyPDF2.PdfFileReader(file2)
   print(f' The file has {reader.numPages} page(s).')

 with open('wtr.pdf','rb') as file3:
   reader = PyPDF2.PdfFileReader(file3)
   print(f' The file has {reader.numPages} page(s).')

 with open('dummy.pdf','rb') as file:
   reader = PyPDF2.PdfFileReader(file)
   page = reader.getPage(0)
   page.rotateClockwise(90)
   writer = PyPDF2.PdfFileWriter()
   writer.addPage(page)
   with open('tilt-file.pdf','wb') as new_file:
     writer.write(new_file)

pdf_file = "./twopage.pdf"
watermark = "./wtr.pdf"
merged_file = "./merged.pdf"

input_file = open(pdf_file, 'rb')
input_pdf = PyPDF2.PdfFileReader(pdf_file)

watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

pdf_page = input_pdf.getPage(0)
watermark_page = watermark_pdf.getPage(0)

pdf_page.mergePage(watermark_page)

output = PyPDF2.PdfFileWriter()
output.addPage(pdf_page)


merged_file = open(merged_file,'wb')
output.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()