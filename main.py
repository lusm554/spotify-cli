import click
from decouple import config as cfg
from reqs import API

@click.group()
def main():
    '''Set API SDK'''
    global api 
    TOKEN = cfg('TOKEN')
    try:
        api = API(TOKEN)
    except ValueError as e:
        print('The access token expired. U need to renew your token.')
        # return status 126 when command is found but is not executable
        exit(126)
    print(f'You\'re logged in like {api.user["display_name"]}')


@main.command('start', help='play track')
def start():
    pass

@main.command('stop', help='stop track')
def stop():
    pass

@main.command('next', help='play next')
def next():
    pass
    
@main.command('curr', help='what track is playing now')
def curr():
    pass

@main.command('prev', help='play previous track')
def prev():
    pass

if __name__ == '__main__':
    main(prog_name='spot')
