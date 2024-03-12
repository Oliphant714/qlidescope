#Restarts the queue
#   Remove every song in the queue, except the NOW_PLAYING
my_list = ['song', 'tune', 'recicitation', 'poem']

def clear_queue(my_list):
    now_playing = my_list[0]
    my_list.clear()
    my_list.append(now_playing)
    #assign position 0 to a variable
    #clear the list
    #variable = position 0
clear_queue(my_list)
print(my_list)