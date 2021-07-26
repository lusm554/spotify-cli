import requests


class API:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        self.s = requests.Session()
        self.s.headers.update(self.headers)
        self.user = self.__user_current_profile__()
    
    def __url__(self, api='', path=''):
        '''Helper for concating API urls'''
        return f'https://api.spotify.com/v1/me{api}{path}'

    def __user_current_profile__(self):
        '''Fetch current user's data'''
        r = self.s.get(self.__url__())
        if r.status_code != 200:
            raise ValueError(r.json())
        return r.json() 

    def current_playback(self):
        r = self.s.get(self.__url__('/player')) 
        if r.status_code != 200:
            raise ValueError(f'User\'s Current Playback {r.status_code}')
        json = r.json()
        return json

    def current_playing_track(self):
        r = self.s.get(self.__url__('/player', '/currently-playing'))
        if r.status_code != 200 or not r.headers.get('content-type') == 'application/json':
            raise ValueError(f'User\'s Currently Playing Track {r.status_code}')
        json = r.json()
        return json
    
    def skip_to_next(self):
        r = self.s.post(self.__url__('/player', '/next'))
        if r.status_code != 204:
            raise ValueError(r.json())
        return r.status_code

