
def clear_queue(queue):
    global song_count
    song_count = 0
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue

def add_playlist(playlist, queue):
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

def count_songs(queue, start_over = False):
    song_count = 0
    num_songs_to_play = len(queue)
    counted_songs = list(queue)
    while num_songs_to_play > song_count:
        song_count =+ 1
        display()
    clear_queue(queue)
    if start_over == True:
        add_playlist(counted_songs)

def display(queue):
    for song in queue:
        print(f"Now playing: {song}")

def start(playlist, number_of_iterations):
    




def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    lines = content.split('\n')
    return lines
inst_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\instrumental_music_list.md"
instrumental_content = read_md_file(inst_path)
oc_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\owl_city_songs.md"
oc_content = read_md_file(oc_path)

song_queue = add_playlist(instrumental_content, [])
display(song_queue)
print(f'Current song count: {song_count}')
start_over = 'on'
display(song_queue)
print(f'Current song count: {song_count}')