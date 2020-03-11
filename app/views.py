from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Create your views here.

TTL = 60 * 120
MATTER_MOST_URL = 'https://mattermost-namnlnh.herokuapp.com/api/v4/'
INTERCOM_APP_ID = 'j0pnttcr'
INTERCOM_PING_URL = 'https://api-iam.intercom.io/messenger/web/ping'

def hello_world(request):
  d = {
    'user_id': '1231312',
    'user_name': 'phmtuan'
  }
  print(cache.set('1', d, timeout=7200))
  print(cache.get('1'))
  print(cache.ttl('1'))
  return HttpResponse('Hello World')

@api_view(['POST'])
def recieve_intercom_hook(request):
  user = request.data['data']['item']['user']
  user_id = user['id']
  cache.set(user_id, user, timeout=TTL)
  return Response({'data': request.data})

@api_view(['GET'])
def ping_intercom():
  req_data = {
    'app_id' = INTERCOM_APP_ID
  }
  res = requests.post(url=INTERCOM_PING_URL,json=req_data)
  res_json = res.json()
  user_id = res_json.user.id
  user


@api_view(['GET'])
def send_message_to_intercom():
