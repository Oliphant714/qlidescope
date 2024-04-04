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

#Function actually is an iteration count, not a song count
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
            

def display(queue):
    for song in queue:
        print(f"Now playing: {song}")
    

def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    lines = content.split('\n')
    return lines





inst_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\instrumental_music_list.md"
inst_content = read_md_file(inst_path)
oc_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\owl_city_songs.md"
oc_content = read_md_file(oc_path)
dis_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\disney.md"
dis_content = read_md_file(dis_path)

queue = []
add_playlist(queue, dis_content)
iterations(queue, 3)