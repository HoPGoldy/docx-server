# docx-server

基于 python3 的 office word 的自动生成服务器的基本框架。

# 简介

本项目整合了 python-docx 和 flask, 并完成了一个轻量的服务器结构 ( `flask` + `gunicorn` + `nginx` ), 你可以使用本项目快速部署一个自动生成服务器的 demo 并发布成 docker 镜像。

然而作为一个"基本"框架, 本项目并没有完成多少可用功能, *而是提供了一些常用示例*, 这要求你拥有一定的 python 基础和对上述两个主要模块的使用经验。然后你可以在本框架的基础上完成你的需求。

# 需求

- python `>3.7.2`

# 安装依赖

```
pip3 install -r requirements.txt
```

# 启动开发服务器

```
python src/app.py
```

# 测试

访问 `http://localhost:5000`，会自动下载 `helloWorld.docx` 文件

# docker 构建

构建镜像:

```
docker build -t docx-server .
```

启动容器:

```
docker run -d -p 5000:80 --name docx docx-server
```

# 开始动手!

本项目完成了项目的部署流程, 所以你可以把开发精力放在以下两部分:

- **接口实现**: 通过将自定义的 url 接口添加到 `src/app.py`, 你可以实现诸如将给定参数插入到文档的功能
- **word 生成**: 在 `src/docxCreater/` 下新建你的文档生成模块, 并在 `src/app.py` 中引入以在接口中使用它。

# 项目结构

```
/src ------------------------------ 源代码目录
  ├─ /docxCreater ----------------- 文档生成模块存放目录
  │   └─ helloWorld --------------- 示例模块
  │        └─ main.py ------------- 示例模块主函数入口
  ├─ app.py ----------------------- flask 路由文件
  └─ wsgi.py ---------------------- gunicorn 部署文件
nginx_setting --------------------- nginx 配置文件
requirements.txt ------------------ 项目依赖
Dockerfile ------------------------ docker 构建文件
start.sh -------------------------- docker 启动脚本
```