#!/bash/bin

# 清理本地的python 缓存命令
find . -type f | grep __py | xargs rm -rf



curl http://127.0.0.1:5000/healz


# 请求问题

curl -X POST -H 'content-type: application/json' -d '{"q": "请给我讲一个笑话吧"}' 'http://127.0.0.1:5000/q'
