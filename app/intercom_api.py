import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

@api_view
def get_message_detail_from_mattermost(message_id):
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

INTERCOM_URL = https://api.intercom.io

@api_view(['POST'])
def reply_conversation(token,message):
    end_point = 'conversations/{}/reply'
    req_url = '{}/{}'.format(INTERCOM_URL,end_point)
    req_data = {
        'message_type': 'comment',
        'type' : 'admin',
        'admin_id': admin_id,
        'body': message
    }
    req_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
  }