import io


def save(doc):
    '''
    将 docx 对象转换为文件流
    ARGS:
        doc: 文档对象
    RETURNS:
        fileStream: 文档的 io 流
    '''
    fileStream = io.BytesIO()
    doc.save(fileStream)
    fileStream.seek(0)

    return fileStream


def replace_text(doc, old_text, new_text):
    '''
    全文内容替换
    ARGS:
        doc: 文档对象
        old_text: 被替换的文本
        new_text: 替换成的文本
    '''
    # 遍历每个段落
    for p in doc.paragraphs:
        # 如果要搜索的内容在该段落
        if old_text in p.text:
            # 使用 runs 替换内容但不改变样式
            # 注意！runs 会根据样式分隔内容，确保被替换内容的样式一致
            for run in p.runs:
                if old_text in run.text:
                    run.text = run.text.replace(old_text, new_text)