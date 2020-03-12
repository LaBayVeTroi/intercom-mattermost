import requests
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .intercom_api import reply_conversation

TOKEN_ADMIN_INTERCOM = 'dG9rOjI0OWE3N2Q1X2Q1MTRfNDQzM184YmUzX2U5YjAyNWY1MzcxZToxOjA='

@api_view(['POST'])
def recieve_mattermost_hook(request):
  message_id = request.data['post_id']
  message = request.data['text']
  user_id = request.data['user_name']
  user = cache.get(user_id)
  token = user['token_mattermost']
  reply_conversation(TOKEN_ADMIN_INTERCOM,message)
  return Response({'data': 'success'})