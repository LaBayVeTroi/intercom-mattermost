import requests
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mattermost_api import (
  create_user,
  login,
  add_user_to_team,
  add_user_to_channel,
  forward_message_to_mattermost,
)
from django.core.cache import cache

CACHE_TTL = 120 * 60

@api_view(['POST'])
def recieve_intercom_hook(request):
  user = request.data['data']['item']['user']
  conversation_id = request.data['data']['item']['id']
  user_id = user['id']
  user_cache = cache.get(user_id)
  root_message_id = ''
  if (user_cache is None):
    mattermost_id = create_user(user_id)
    add_user_to_team(mattermost_id)
    add_user_to_channel(mattermost_id)
    user['mattermost_id'] = mattermost_id
    message = request.data['data']['item']['conversation_message']['body']
  else :
    root_message_id = user_cache['root_message_id']
    message = request.data['data']['item']['conversation_parts']['conversation_parts'][0]['body']
  token_mattermost = login(user_id)
  user['token_mattermost'] = token_mattermost
  message_detail = forward_message_to_mattermost(token_mattermost,root_message_id,message)
  if(root_message_id == ''):
    user['root_message_id'] = message_detail['id']
    user['conversation_id'] = conversation_id
    cache.set(user_id, user, timeout=CACHE_TTL)
 
  return Response({'data': request.data})