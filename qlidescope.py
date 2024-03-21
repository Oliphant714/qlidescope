queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']
removed_song = ['tune']
loop = 'off'

def clear_queue(queue = queue):
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue

# Adds playlist to the END of the queue
def add_playlist(playlist, queue = queue):
    new_songs = [song for song in playlist if song not in queue]
    queue.extend(new_songs)
    return queue
    # Ignores repeat songs

def looping(loop, queue = queue):
    stored_songs = list(queue)
    while loop == 'on':
        if queue:
            now_playing = queue[0]
            print("Now playing:", now_playing)
        else:
            print("Queue is empty. No song to play.")
            return stored_songs
    for song in queue:
        print (f"Now playing {song}")
    return stored_songs

add_playlist(second_list)
looping('on')
print(queue)
looping('off')
print(queue)