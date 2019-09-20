from flask import Blueprint
from ..utils import send
# 引入 word 生成模块
from docxCreater import helloworld_create

# 新建蓝图
router = Blueprint('download', __name__)


@router.route('/')
def download_file():
    # 获取 word 的文件流
    file_stream = helloworld_create()
    # 转换成下载
    return send(file_stream, 'helloWorld.docx')