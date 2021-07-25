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
        if 'error' in self.user:
            raise ValueError(self.user['error']['message'])

    
    def __url__(self, api='', path=''):
        '''Helper for concating API urls'''
        return f'https://api.spotify.com/v1/me{api}{path}'

    def __user_current_profile__(self):
        '''Fetch current user's data'''
        r = self.s.get(self.__url__())
        return r.json() 

    def current_playback(self):
        r = self.s.get(self.__url__('/player')) 
        json = r.json()
        for k, v in json.items():
            print(k, v) 
    
    def skip_to_next(self):
        r = self.s.post(self.__url__('/player', '/next'))
        if r.status_code != 204:
            return r.json()
        return r.status_code

