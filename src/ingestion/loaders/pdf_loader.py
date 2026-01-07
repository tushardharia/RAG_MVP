import PyPDF2

def load_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for i in range(len(reader.pages)):
            text += reader.pages[i].extract_text()
        return text