# Creation of this code was accelerated using ChatGPT
from itertools import zip_longest
from random import randint
def add_playlist(song_queue, *playlists):
  """
  Adds songs from one or more playlists to the music queue if they are not already in the queue,
  shuffling the order of the added songs.

  Parameters:
  - song_queue (list): A list representing the queue of songs.
  - *playlists (lists): Variable number of playlists containing songs to be added to the queue.

  Complexity:
  - Time: O(n * m * l), where n is the number of songs in the longest playlist,
    m is the number of playlists, and l is the average length of each playlist.
    The function iterates through each song in each playlist to check if it's in the queue, taking linear time.
    Additionally, shuffling the merged list takes O(n) time.
  - Space: O(n), where n is the total number of unique songs across all playlists.
    The function creates a merged list of songs to be added, potentially occupying additional memory.

  Returns:
  - list: The modified song queue with added songs from the playlists in shuffled order.
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