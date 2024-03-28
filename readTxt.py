import PyPDF2

def extract_text_from_pdf(pdf_path, page_numbers=[]):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for pageNum in range(len(pdf_reader.pages)):
            if pageNum in page_numbers:
                page = pdf_reader.pages[pageNum]
                text += page.extract_text()
    return text

pdf_txt = extract_text_from_pdf('manteau.pdf', [4,58])

