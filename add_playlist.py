# Creation of this code was accelerated using ChatGPT
from itertools import zip_longest
from random import randint
def add_playlist(song_queue, *playlists):
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
  zipped_lists = zip_longest(*playlists)
  merged_list = [item for pair in zipped_lists for item in pair if item is not None and item not in song_queue]
  
  def shuffled_songs(playlist):
    shuffled_list = list(playlist)
    n = len(shuffled_list)
    for i in range(n-1, 0, -1):
      j = randint(0, i+1)
      shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
    return shuffled_list
  adding_songs = shuffled_songs(merged_list)
  song_queue.extend(adding_songs)
  return song_queue


first_list = ['song', 'tune', 'recicitation', 'poem']
second_list = ['Happy', 'Sneezy', 'Bashful', 'Doc', 'Sleepy', 'Dopey', 'Grumpy']

song_queue = add_playlist([], first_list, second_list)
print(song_queue)
song_queue = add_playlist([], song_queue)
print(song_queue)
