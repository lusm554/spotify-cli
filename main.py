import sys
import requests
import base64

args = sys.argv[1:]
print(f'{args=}')

# Client Credentials Flow
token_url = 'https://accounts.spotify.com/api/token'
# tokens from spotify app 
client_id = ''
client_secret = ''

auth_token = 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode('ascii')).decode('ascii')
headers = {
    #'Authorization': f'Basic {client_id}:{client_secret}',
    'Authorization': auth_token,
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'client_credentials'
}
res = requests.post(token_url, data=data, headers=headers)
json = res.json()
token = json['access_token']
print(json)

h = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

#res = requests.post('https://api.spotify.com/v1/me/player/previous', headers=h)
#print(res.json())


res = requests.get('https://api.spotify.com/v1/me/player/devices', headers=h)
print(res.json())
