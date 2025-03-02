
from flask import Flask
from flask_restful import Api
from src.handlers.sysplat import healz
from src.handlers.chat import question

# 初始化api
app = Flask(__name__)
api = Api(app)

app.config['JSON_AS_ASCII'] = False

api.add_resource(healz.HealthCheckHandler, '/healz')     # 健康检查

api.add_resource(question.QuestionHandler, '/q')     # 问答


