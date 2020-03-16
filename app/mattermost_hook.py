import requests
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .intercom_api import reply_conversation
from django.core.cache import cache

from .mattermost_api import (
  get_post_detail,
  get_user_detail
)


@api_view(['POST'])
def recieve_mattermost_hook(request):
  data = request.data
  post_id = data.get('post_id')
  message = data.get('text')
  post_detail = get_post_detail(post_id)
  user_id = post_detail.get('user_id')
  user_detail = get_user_detail(user_id)
  mattermost_username = user_detail.get('username')
  integrate_user = cache.get(mattermost_username)
  send_message_to_intercom = {'message': 'faild or newuser'}
  if integrate_user is not None:
    conversation_id = integrate_user.get('conversation')['id']
    send_message_to_intercom = reply_conversation(conversation_id, message)
  print(integrate_user)
  return Response(send_message_to_intercom)



