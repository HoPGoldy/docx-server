from flask import Flask
# 路由引入
from router.helloWorld import download
# 新建实例
app = Flask(__name__)
# 注册路由
app.register_blueprint(download, url_prefix='/download')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')