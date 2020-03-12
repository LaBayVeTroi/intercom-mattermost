import requests
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .intercom_api import get_message_detail_from_mattermost

@api_view(['POST'])
def recieve_mattermost_hook(request):
  message_id = request.data['post_id']
  user_id = request.data['user_name']
  user = cache.get(user_id)
  token = user['token_mattermost']
  message_detail = get_message_detail_from_mattermost(token,message_id)
  if(user['message'])
  return Response({'data': 'success'})