# docx-server
基于 python3 的 office word 的自动生成服务器

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

访问 `http://127.0.0.1:5000/`，会自动下载 `helloWorld.docx` 文件

# docker 构建

构建镜像:

```
docker build -t docx-server .
```

启动容器:

```
docker run -d -p 5000:80 --name docx docx-server
```