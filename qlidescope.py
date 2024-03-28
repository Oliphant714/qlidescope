queue = []
loop = 'off'
song_count = 0
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    lines = content.split('\n')
    return lines
inst_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\instrumental_music_list.md"
instrumental_content = read_md_file(inst_path)
oc_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\owl_city_songs.md"
oc_content = read_md_file(oc_path)

def display(queue = queue):
    global song_count
    song_count = 0
    for song in queue:
        song_count += 1
        print(f"Now playing: {song}")
        

def clear_queue(queue = queue):
    global song_count
    song_count = 0
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue

def add_playlist(playlist, queue = queue):
    from random import randint
    def shuffled_songs(playlist = playlist):
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

