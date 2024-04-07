import PyPDF2

def read_pdf(pdf):
    with open("pdf_reader.py","rb") as pdf:
        pdf_reader=PyPDF2.PdfReader(pdf)
        pages=pdf_reader.numPages

        for page in range(pages):
            page=pdf_reader.getPage(page)
            text=page.extractText()

        print(text)


read_pdf("c4611_sample_explain.pdf")