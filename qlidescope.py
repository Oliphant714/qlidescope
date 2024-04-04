# Creation of this code was accelerated using ChatGPT

def display(queue):
    """
    Displays the songs in the music queue.

    Parameters:
    - queue (list): A list representing the queue of songs.

    Complexity:
    - Time: O(n), where n is the number of songs in the queue.
      The function iterates through each song in the queue to display it.
    - Space: O(1)
      The function operates in constant space regardless of the size of the queue.

    Returns:
    - None
    """
    for song in queue:
        print(f"Now playing: {song}")
        
def clear_queue(queue):
    """
    Clears the music queue except for the currently playing song.

    Parameters:
    - queue (list): A list representing the queue of songs.

    Complexity:
    - Time: O(n), where n is the number of songs in the queue.
      The function clears the queue and appends the currently playing song, both taking linear time.
    - Space: O(1)
      The function operates in constant space regardless of the size of the queue.

    Returns:
    - list: The modified queue with only the currently playing song.
    """
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue

def add_playlist(queue, playlist):
    """
    Adds songs from a playlist to the music queue if they are not already in the queue,
    shuffling the order of the added songs.

    Parameters:
    - queue (list): A list representing the queue of songs.
    - playlist (list): A list of songs to be added to the queue.

    Complexity:
    - Time: O(n * m), where n is the number of songs in the playlist and m is the number of songs in the queue.
      The function iterates through each song in the playlist to check if it's in the queue, taking linear time.
      Additionally, shuffling the new songs takes O(n) time.
    - Space: O(n), where n is the number of songs in the playlist.
      The function creates a list of new songs to be added, potentially occupying additional memory.

    Returns:
    - list: The modified queue with added songs from the playlist in shuffled order.
    """
    from random import randint
    def shuffled_songs(playlist):
        """
    Shuffles the order of songs in a playlist.

    Parameters:
    - playlist (list): A list of songs to be shuffled.

    Complexity:
    - Time: O(n), where n is the number of songs in the playlist.
      The function iterates through each song in the playlist to shuffle its position.
    - Space: O(n), where n is the number of songs in the playlist.
      The function creates a shuffled list of songs, potentially occupying additional memory.

    Returns:
    - list: The playlist with songs shuffled.
    """
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

def looping(queue, loop = False):
    """
    Simulates looping a specific song until loop is turned off.

    Parameters:
    - queue (list): A list representing the queue of songs to be played.
    - loop (bool): Represents the state of looping. If True, continues looping; otherwise, stops. Default is False.

    Complexity:
    - Time: O(n), where n is the number of songs in the queue.
      The function iterates through the queue once to print the now playing songs.
    - Space: O(n), where n is the number of songs in the queue.
      A copy of the queue is stored in 'stored_songs', occupying additional memory.

    Returns:
    - list: A copy of the original queue.
    """
    stored_songs = list(queue)
    while loop == True:
        if queue:
            now_playing = queue[0]
            display(now_playing)
        else:
            print("Queue is empty. No song to play.")
            return stored_songs
    display(queue)
    return stored_songs

def iterations(queue, iterations, start_over = False):
    """
    Simulates playing through a music queue for a certain number of iterations.

    Parameters:
    - queue (list): A list representing the queue of songs to be played.
    - iterations (int): The number of iterations to play through the queue.
    - start_over (bool): Indicates whether to start over the queue after completing all iterations. Default is False.

    Complexity:
    - Time: O(n * m), where n is the number of songs in the queue and m is the number of iterations.
      The function iterates through the queue and adds songs in each iteration, taking linear time.
    - Space: O(n), where n is the number of songs in the queue.
      The function creates a copy of the queue, potentially occupying additional memory.

    Returns:
    - None
    """
    iter_count = 0
    counted_songs = list(queue)
    while iterations > iter_count:
        iter_count += 1
        display(queue)
        queue.clear()
        queue = add_playlist(queue, counted_songs)
        if start_over == True and iter_count == iterations:
            iter_count = 0