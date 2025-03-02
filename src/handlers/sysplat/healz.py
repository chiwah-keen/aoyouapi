

from flask_restful import Resource
from src.consts import respcode
from src.handlers.resp import JsonResponse

class HealthCheckHandler(Resource):
    def get(self):
        return JsonResponse().set(respcode.SUCCESS)



