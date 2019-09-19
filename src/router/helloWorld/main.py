from flask import Blueprint, send_file
from urllib.parse import quote
# 引入 word 生成模块
from docxCreater.helloWorld import helloworld_create
# 新建蓝图
download = Blueprint('download', __name__)

@download.route('/')
def download_file():
    # 获取 word 的文件流
    file_stream = helloworld_create()
    filename = quote('helloWorld.docx')
    # 新建文件下载
    rv = send_file(file_stream, as_attachment=True, attachment_filename=filename)
    rv.headers['Content-Disposition'] += f'; filename*=utf-8''{filename}'
    return rv