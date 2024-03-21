# Creation of this code was accelerated using ChatGPT

queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']

def add_playlist(playlist, queue = queue):
    """
    Adds songs from a playlist to the music queue if they are not already in the queue.

    Parameters:
    - playlist (list): A list of songs to be added to the queue.
    - queue (list): A list representing the queue of songs.

    Complexity:
    - Time: O(n * m), where n is the number of songs in the playlist and m is the number of songs in the queue.
      The function iterates through each song in the playlist to check if it's in the queue, taking linear time.
      Appending songs to the queue takes constant time.
    - Space: O(n), where n is the number of songs in the playlist.
      The function creates a list of new songs to be added, potentially occupying additional memory.

    Returns:
    - list: The modified queue with added songs from the playlist.
    """
    new_songs = [song for song in playlist if song not in queue]
    queue.extend(new_songs)
    return queue