# Creation of this code was accelerated using ChatGPT

def display(queue):
    for song in queue:
        print(f"Now playing: {song}")
        
def clear_queue(queue):
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue

def add_playlist(queue, playlist):
    from random import randint
    def shuffled_songs(playlist):
        shuffled_list = list(playlist)  
        n = len(shuffled_list)
        for i in range(n-1, 0, -1):
            j = randint(0, i+1)
            shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
        return shuffled_list
    new_songs = [song for song in playlist if song not in queue]
    adding_songs = shuffled_songs(new_songs)
    queue.extend(adding_songs)
    return queue

def looping(loop, queue):
    stored_songs = list(queue)
    while loop == 'on':
        if queue:
            now_playing = queue[0]
            display(now_playing)
        else:
            print("Queue is empty. No song to play.")
            return stored_songs
    display(queue)
    return stored_songs

def iterations(queue, iterations, start_over = False):
    iter_count = 0
    counted_songs = list(queue)
    while iterations > iter_count:
        iter_count += 1
        display(queue)
        queue.clear()
        queue = add_playlist(queue, counted_songs)
        if start_over == True and iter_count == iterations:
            iter_count = 0