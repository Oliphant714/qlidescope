queue = []
loop = 'off'
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    lines = content.split('\n')
    return lines
inst_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\instrumental_music_list.md"  # Replace 'example.md' with the path to your Markdown file
instrumental_content = read_md_file(inst_path)
oc_path = r"C:\\Users\\Isaac\\OneDrive\\Documents\\Semester 3\\functions\\qlidescope\\owl_city_songs.md"
oc_content = read_md_file(oc_path)


def display(queue = queue):
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

display(oc_content)