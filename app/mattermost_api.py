import requests

MATTER_MOST_URL = 'https://mattermost-namnlnh.herokuapp.com/api/v4'
PASSWORD_CREATE_USER = '123456'
TOKEN_ADMIN_MATTERMOST = '51sdzcjrojnudeymx9z7zoitbe'
TEAM_ID = 'soqngurrzp8pzx7gt1ojwymsrr'


# Create user
def create_user(user_id):
  req_data = {
    'email': '{}@gmail.com'.format(user_id),
    'username': '{}'.format(user_id),
    'password': PASSWORD_CREATE_USER
  }
  end_point = '/users'
  req_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(TOKEN_ADMIN_MATTERMOST)
  }
  req_url = '{}/{}'.format(MATTER_MOST_URL, end_point)
  res = requests.post(url=req_url, headers=req_headers, json=req_data)
  res_json = res.json()
  id_logged_in = res_json.id
  token_mattermost = login(id_logged_in)



def login(id_logged_in):
  req_data = {
    'login_id': id_logged_in,
    'password': PASSWORD_CREATE_USER
  }
  end_point = '/users/login'
  req_url = '{}/{}'.format(MATTER_MOST_URL, end_point)
  res = requests.post(url=req_url, json=req_data)
  res_json = res.json()
  
