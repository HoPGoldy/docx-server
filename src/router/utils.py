from flask import send_file
from urllib.parse import quote


def send(stream, name):
    '''
    将文件流转化成文件下载
    '''
    filename = quote(name)
    # 新建文件下载
    rv = send_file(stream, as_attachment=True, attachment_filename=filename)
    rv.headers['Content-Disposition'] += f'; filename*=utf-8''{filename}'
    return rv