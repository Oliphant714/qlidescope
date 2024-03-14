queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']
removed_song = ['tune']

#Restarts the queue
#   Remove every song in the queue, except the NOW_PLAYING
def clear_queue(queue):
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue
    # Position [0] is Now Playing

# Adds playlist to the END of the queue and ignores any repeat songs
def add_playlist(playlist, queue = queue):
    queue.extend(playlist)
    return queue


add_playlist(first_list)
print(queue)

clear_queue(queue)
print(queue)

add_playlist(second_list)
add_playlist(first_list)
print(queue)