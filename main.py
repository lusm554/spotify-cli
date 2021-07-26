import click
from decouple import RepositoryEnv, Config
from reqs import API
import time
import os


@click.group()
def main():
    '''Set API SDK'''
    global api 
    path_to_env = os.environ.get('SPOT_TOKEN_PATH')
    if not path_to_env:
        print('Set SPOT_TOKEN_PATH env')
        exit(1)
    env = Config(RepositoryEnv(path_to_env)) 
    TOKEN = env.get('TOKEN')
    try:
        api = API(TOKEN)
    except ValueError as e:
        msg = str(e)
        print(msg)
        if msg == 'The access token expired':
            # return status 126 when command is found but is not executable
            exit(126)
        exit(1)
    print(f'You\'re logged in like {api.user["display_name"]}')

def __pretty__(track):
    '''Creats pretty form of track'''
    name = track['item']['name']
    artists = ', '.join([artist['name'] for artist in track['item']['artists']])
    return '  {} - {}'.format(artists, name)

@main.command('start', help='play track')
def start():
    pass

@main.command('stop', help='stop track')
def stop():
    try:
        api.pause_playback()
        track = api.current_playback()
        print(track)
    except ValueError as e:
        print(e)
        exit(1)
    print('Stopped:')
    print(__pretty__(track))

@main.command('next', help='play next')
def next():
    try:
        r = api.skip_to_next()
        curr = api.current_playback()
    except ValueError as e:
        print(e)
        exit(1)
    curr_track_id = curr['item']['id']
    while 1:
        next_track = api.current_playback()
        if curr_track_id != next_track['item']['id']:
            curr = next_track
            break
        time.sleep(1.5)
    print('Now playing:')
    print(__pretty__(curr))
    
@main.command('curr', help='what track is playing now')
def curr():
    pass

@main.command('prev', help='play previous track')
def prev():
    pass

if __name__ == '__main__':
    main(prog_name='spot')
