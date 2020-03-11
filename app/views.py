from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

TTL = 60 * 120
MATTER_MOST_URL = 'https://mattermost-namnlnh.herokuapp.com/api/v4/'

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

