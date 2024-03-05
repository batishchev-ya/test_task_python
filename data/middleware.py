from .models import Log
import datetime

class LogggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Выполнение кода перед обработкой запроса
        # accept_language = (request.headers['Accept-Language']).split('-', 1)[0]
        # new_log = Log(time=datetime.datetime.now(), ip=request.META['REMOTE_ADDR'], user_agent=request.META['HTTP_USER_AGENT'], accept_language = accept_language)
        # new_log.save()
        response = self.get_response(request)
        # Выполнение кода после обработки запроса и перед возвратом ответа
        return response

