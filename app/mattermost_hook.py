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
  root_detail = get_post_detail(post_detail.get('root_id'))
  user_id = root_detail.get('user_id')
  user_detail = get_user_detail(user_id)
  mattermost_username = user_detail.get('username') #intercom_username
  integrate_user = cache.get(mattermost_username)
  send_message_to_intercom = {'message': 'faild or newuser'}
  if integrate_user is not None:
    conversation_id = integrate_user.get('conversation_id')
    send_message_to_intercom = reply_conversation(conversation_id, message)
  return Response(send_message_to_intercom)
