from flask_restful import Resource, request
from src.consts import respcode
from src.handlers.resp import JsonResponse
from src.conf import conf
from src.services.chat import chat_service

class QuestionHandler(Resource):
    def post(self):
        question = request.json.get("q")
        if not question:
            return JsonResponse().set(respcode.VALIDATE_PARAMS_ERROR)
        if not conf.CHAT_SERVERS:
            return JsonResponse().set(respcode.SERVER_RESOURECE_ERROR)
        answer = chat_service.ask(question)
        return JsonResponse().set(respcode.SUCCESS, data=answer)