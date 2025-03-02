
import json
from flask import Response

RSP_TYPE_JSON = "application/json; charset=utf-8"

class JsonResponse(dict):

    def __init__(self):
       pass

    def set(self, status_message, data=""):
        resp_data = {"status": status_message[0], "message": status_message[1], "data": data}
        resp_str = json.dumps(resp_data, ensure_ascii=False)
        return Response(resp_str, status = 200 , content_type=RSP_TYPE_JSON)

class AbortJsonResonse(dict):

    def __init__(self):
        pass

    def set(self, http_status, status_message, data=""):
        resp_data = {"status": status_message[0], "message": status_message[1], "data": data}
        resp_str = json.dumps(resp_data, ensure_ascii=False)
        return Response(resp_str, status = http_status , content_type=RSP_TYPE_JSON)