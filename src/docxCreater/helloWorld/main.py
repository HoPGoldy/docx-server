from docx import Document
from ..utils import save


def create():
    '''
    基本示例, 执行此方法即可获取文档流
    RETURNS:
        fileStream: 文档的 io 流
    '''
    document = Document()
    document.add_paragraph('Hello World!')
    return save(document)