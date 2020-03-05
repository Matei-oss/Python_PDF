#PYTHON PDF's

import PyPDF2 

#rb - read binary

with open('dummy.pdf','rb') as file:
  reader = PyPDF2.PdfFileReader(file)
  print(f' The file has {reader.numPages} pages.')

with open('twopage.pdf','rb') as file2:
  reader = PyPDF2.PdfFileReader(file2)
  print(f' The file has {reader.numPages} pages.')

with open('wtr.pdf','rb') as file3:
  reader = PyPDF2.PdfFileReader(file3)
  print(f' The file has {reader.numPages} pages.')

with open('dummy.pdf','rb') as file1:
  reader = PyPDF2.PdfFileReader(file1)
  page = reader.getPage(0)
  page.rotateClockwise(90)
  writer = PyPDF2.PdfFileWriter()
  writer.addPage(page)
  with open('tilt.pdf','wb') as new_file:
    writer.write(new_file)