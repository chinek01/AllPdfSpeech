from PyPDF2 import PdfReader

reader = PdfReader("pdf_example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

text2 = page.extractText()

print(text2)

