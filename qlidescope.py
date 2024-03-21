queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']
loop = 'off'

def clear_queue(queue = queue):
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue

def add_playlist(playlist, queue = queue):
    from random import randint
    def shuffle_strings(string_list):
        shuffled_list = list(string_list)  # Make a copy of the original list
        n = len(shuffled_list)
        for i in range(n-1, 0, -1):
            j = randint(0, i+1)
            shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
        return shuffled_list
    new_songs = [song for song in playlist if song not in queue]
    adding_songs = shuffle_strings(new_songs)
    queue.extend(adding_songs)
    return queue

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