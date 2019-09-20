from docx import Document
import time
from ..utils import save, replace_text
from .config import DEFAULT


def create(title, content, author):
    '''
    使用参数和模板生成文档
    ARGS:
        title: 标题
        content: 正文
        author: 名称
    RETURNS:
        fileStream: 文档的 io 流
    '''
    doc = Document('./src/docxCreater/createWithTemplate/template.docx')

    replace_text(doc, '{{title}}', title or DEFAULT['title'])
    replace_text(doc, '{{content}}', content or DEFAULT['content'])
    replace_text(doc, '{{date}}', time.strftime('%Y-%m-%d', time.localtime(time.time())))
    replace_text(doc, '{{name}}', author or DEFAULT['author'])
    
    return save(doc)