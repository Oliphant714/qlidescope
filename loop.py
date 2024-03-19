queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']
loop = 'off'

def looping(loop = loop, queue = queue):
    stored_songs = queue
    if loop == 'on':
        now_playing = queue[0]
        queue = now_playing
        return queue
    else:
        queue = stored_songs
        return queue