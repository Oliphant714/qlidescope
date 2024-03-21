# Creation of this code was accelerated using ChatGPT

queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']


def clear_queue(queue = queue):
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