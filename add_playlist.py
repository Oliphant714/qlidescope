# Creation of this code was accelerated using ChatGPT

queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']

def add_playlist(playlist, queue = queue):
    """
    Adds songs from a playlist to the music queue if they are not already in the queue,
    shuffling the order of the added songs using the Fisher-Yates suffle Algorithm.

    Parameters:
    - playlist (list): A list of songs to be added to the queue.
    - queue (list): A list representing the queue of songs.

    Complexity:
    - Time: O(n * m), where n is the number of songs in the playlist and m is the number of songs in the queue.
      The function iterates through each song in the playlist to check if it's in the queue, taking linear time.
      Appending songs to the queue takes constant time.
      Additionally, shuffling the new songs takes O(n) time.
    - Space: O(n), where n is the number of songs in the playlist.
      The function creates a list of new songs to be added, potentially occupying additional memory.

    Returns:
    - list: The modified queue with added songs from the playlist in shuffled order.
    """
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

add_playlist(first_list)
print(queue)
add_playlist(second_list)
print(queue)
