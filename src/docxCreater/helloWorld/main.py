from docx import Document
import io

def create():
    document = Document()
    document.add_paragraph('Hello World!')
    return save(document)

def save(document):
    fileStream = io.BytesIO()
    document.save(fileStream)
    fileStream.seek(0)

    return fileStream