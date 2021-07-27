import requests


class API:
    '''
    Class that wraps Spotify REST API into python methods.
    '''

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

    def pause_playback(self):
        '''Pause playback on the user’s account.'''
        r = self.s.put(self.__url__('/player', '/pause'))
        if r.status_code != 204:
            raise ValueError(f'Pause a User\'s Playback {r.status_code}')
        return r.status_code

    def start_resume_playback(self):
        '''Start a new context or resume current playback
        on the user’s active device.'''
        r = self.s.put(self.__url__('/player', '/play'))
        if r.status_code != 204:
            raise ValueError(f'Start/Resume User\'s Playback {r.status_code}')
        return r.status_code

    def current_playback(self):
        '''Get information about the user’s current playback state,
        including track or episode, progress, and active device.'''
        r = self.s.get(self.__url__('/player'))
        if r.status_code != 200:
            raise ValueError(f'User\'s Current Playback {r.status_code}')
        json = r.json()
        return json

    def current_playing_track(self):
        '''Get the object currently being played
        on the user’s Spotify account.'''
        r = self.s.get(self.__url__('/player', '/currently-playing'))
        is_json = r.headers.get('content-type') == 'application/json'
        if r.status_code != 200 or not is_json:
            raise ValueError(

                f'User\'s Currently Playing Track {r.status_code}'
            )
        json = r.json()
        return json

    def skip_to_next(self):
        '''Skips to next track in the user’s queue.'''
        r = self.s.post(self.__url__('/player', '/next'))
        if r.status_code != 204:
            raise ValueError(r.json())
        return r.status_code

    def skip_to_previous(self):
        '''Skips to previous track in the user’s queue.'''
        r = self.s.post(self.__url__('/player', '/previous'))
        if r.status_code != 204:
            raise ValueError(
                f'Skip User’s Playback To Previous Track {r.status_code}'
            )
        return r.status_code
