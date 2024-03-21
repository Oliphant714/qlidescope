# Creation of this code was accelerated using ChatGPT

queue = []
first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']


def clear_queue(queue = queue):
    now_playing = queue[0]
    queue.clear()
    queue.append(now_playing)
    return queue

def looping(loop, queue = queue):
    """
    Simulates a music player that continuously plays songs from a queue until the loop is turned off.

    Args:
    - loop (str): Indicates whether the music player should continue playing songs ('on') or stop ('off').
    - queue (list): A list representing the queue of songs to be played.

    Returns:
    - list: A copy of the original queue of songs.

    Complexity:
    - Time: O(n), where n is the number of songs in the queue. The function iterates through the queue once.
    - Space: O(n), where n is the number of songs in the queue. Additional space is used to store the copied list of songs.

    Notes:
    - The function prints the currently playing song from the queue until the loop is turned off.
    - If the queue is empty, it prints a message indicating so.
    """
    stored_songs = list(queue)  # Make a copy of the queue
    while loop == 'on':
        if queue:  # If the queue is not empty
            now_playing = queue[0]  # Get the first song in the queue
            print("Now playing:", now_playing)  # Replace with your play function
        else:
            print("Queue is empty. No song to play.")
            return stored_songs
    for song in queue:
        print (f"Now playing {song}")
    return stored_songs

#queue.extend(first_list)
print(queue)

# looping('off')

looping('on')

looping('off')