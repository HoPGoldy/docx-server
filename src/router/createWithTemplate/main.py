from flask import Blueprint, request
from ..utils import send
# 引入 word 生成模块
from docxCreater import template_create

# 新建蓝图
router = Blueprint('template', __name__)


@router.route('/', methods=[ "GET", "POST" ])
def download_file():
    # 获取参数
    title = request.args.get("title")
    content = request.args.get("content")
    author = request.args.get("author")
    # 获取 word 的文件流
    file_stream = template_create(title, content, author)
    # 转换成下载
    return send(file_stream, '从模板生成.docx')