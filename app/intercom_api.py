import requests
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

TOKEN_ADMIN_INTERCOM = os.environ.get('TOKEN_ADMIN_INTERCOM')
ADMIN_ID = os.environ.get('ADMIN_ID')

INTERCOM_URL = os.environ.get('INTERCOM_URL')


def reply_conversation(conversation_id, message):
    end_point = '/conversations/{}/reply'.format(conversation_id)
    req_url = '{}/{}'.format(INTERCOM_URL, end_point)
    req_data = {
        'message_type': 'comment',
        'type': 'admin',
        'admin_id': ADMIN_ID,
        'body': message
    }
    req_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(TOKEN_ADMIN_INTERCOM),
        'Accept': 'application/json'
    }

    res = requests.post(url=req_url, headers=req_headers, json=req_data)

    return res.json()
