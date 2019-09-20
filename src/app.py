from flask import Flask
# 路由引入
import router
# 新建实例
app = Flask(__name__)
# 注册路由
app.register_blueprint(router.download, url_prefix='/download')
app.register_blueprint(router.template, url_prefix='/template')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')