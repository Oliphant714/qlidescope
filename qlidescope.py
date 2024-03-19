queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']
removed_song = ['tune']
loop = 'off'
#Restarts the queue
#   Remove every song in the queue, except the NOW_PLAYING
def clear_queue(queue = queue):
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue
    # Position [0] is Now Playing

# Adds playlist to the END of the queue
def add_playlist(playlist, queue = queue):
    new_songs = [song for song in playlist if song not in queue]
    queue.extend(new_songs)
    return queue
    # Ignores repeat songs

def looping(loop = loop, queue = queue):
    stored_songs = queue
    if loop == 'on':
        queue = queue[0]
        return queue
    else:
        queue = stored_songs
        return queue

add_playlist(second_list)
looping('on')
print(queue)
looping('off')
print(queue)