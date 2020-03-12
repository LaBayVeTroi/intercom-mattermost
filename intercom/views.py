from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.core.cache import cache
import redis
from rest_framework.decorators import api_view
import requests
# Create your views here.

INTERCOM_APP_ID = 'j0pnttcr'
INTERCOM_PING_URL = 'https://api-iam.intercom.io'
REFERER_URL = 'file:///C:/Users/PV/Desktop/mattermost-button-example.html'
INTERCOM_API = 'https://api.intercom.io'

@api_view(['GET'])
def ping_intercom(request):
  end_point = 'messenger/web/ping'
  req_data = {
    'app_id' : INTERCOM_APP_ID,
    'referer': REFERER_URL
  }
  res = requests.post(url='{}/{}'.format(INTERCOM_PING_URL,end_point),data=req_data)
  user = res.json()['user']
  print(cache.set(user['id'], user, timeout=7200))
  print(cache.get(user['id']))
  send_message_to_intercom(user,'this is a test message')
  return Response({'data':user['id']})

def send_message_to_intercom(user,message):
    end_point = 'conversations'
    req_data = {
        'app_id' : INTERCOM_APP_ID,
        blocks: [{"type":"paragraph","text":message}],

    }
    res = requests.post(url='{}/{}'.format(INTERCOM_API,end_point),data=req_data)
    print(res.json())
