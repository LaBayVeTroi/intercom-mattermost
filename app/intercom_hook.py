import requests
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mattermost_api import create_user, login, forward_message_to_mattermost

@api_view(['POST'])
def recieve_intercom_hook(request):
  user = request.data['data']['item']['user']
  user_id = user['id']
  user_cache = cache.get(user_id)
  root_message_id = ''
  if (user_cache is None) : 
    mattermost_id = create_user(user_id)
    add_user_to_team(mattermost_id)
    add_user_to_channel(mattermost_id)
    user['mattermost_id'] = mattermost_id
  else :
    root_message_id = user_cache['root_message_id']
  token_mattermost = login(user_id)
  user['token_mattermost'] = token_mattermost
  message = request.data['data']['conversation_message']['body']
  message_detail = forward_message_to_mattermost(token_mattermost,root_message_id,message)
  if(root_message_id == ''):
    user['root_message_id'] = message_detail['id']

  return Response({'data': request.data})