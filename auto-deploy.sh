#! /bin/bash

echo "清除过期镜像"
docker container rm -f docx-server
docker image rm docx-server
echo "重新构建镜像"
docker build -t docx-server .
echo "运行容器"
docker run -d -p 5000:80 --name docx docx-server