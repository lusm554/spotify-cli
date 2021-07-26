import click
from decouple import config as cfg
from reqs import API
import time

@click.group()
def main():
    '''Set API SDK'''
    global api 
    TOKEN = cfg('TOKEN')
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


@main.command('start', help='play track')
def start():
    pass

@main.command('stop', help='stop track')
def stop():
    pass

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
    print('  {} - {}'.format(', '.join([i['name'] for i in curr['item']['artists']]), curr['item']['name']))
    
@main.command('curr', help='what track is playing now')
def curr():
    pass

@main.command('prev', help='play previous track')
def prev():
    pass

if __name__ == '__main__':
    main(prog_name='spot')
