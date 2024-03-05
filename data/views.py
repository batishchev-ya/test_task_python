from django.shortcuts import render
import datetime
from django.http import JsonResponse
from .models import Log

# Create your views here.
def data(request):
  accept_language = (request.headers['Accept-Language']).split('-', 1)[0]
  new_log = Log(time=datetime.datetime.now(), ip=request.META['REMOTE_ADDR'], user_agent=request.META['HTTP_USER_AGENT'], accept_language = accept_language)
  new_log.save()
  data = {
    'ts': int(datetime.datetime.now().timestamp()*1000)
  }
  return JsonResponse(data)