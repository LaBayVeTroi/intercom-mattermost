import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

TOKEN_ADMIN_INTERCOM = 'dG9rOjI0OWE3N2Q1X2Q1MTRfNDQzM184YmUzX2U5YjAyNWY1MzcxZToxOjA='
ADMIN_ID = '3865233'

INTERCOM_URL = 'https://api.intercom.io'

def reply_conversation(conversation_id, message):
    end_point = '/conversations/{}/reply'.format(conversation_id)
    req_url = '{}/{}'.format(INTERCOM_URL,end_point)
    req_data = {
        'message_type': 'comment',
        'type' : 'admin',
        'admin_id': ADMIN_ID,
        'body': message
    }
    req_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(TOKEN_ADMIN_INTERCOM),
        'Accept': 'application/json'
    }

    res = requests.post(url=req_url, headers=req_headers, json=req_data)

    print(res.json())

    return res.json()
