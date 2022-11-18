from time import sleep
import pandas as pd

def progress_bar(current_element, bar_width, list_length):
    '''Print a progress bar
    current_element - current position in list or df during the iteration (int)
    bar_width - the width of the progress bar in number of characters (int)
    list_length - the length of the list or df to iterate (int)
    '''
    percent = current_element / list_length
    left = bar_width * percent
    right = bar_width - int(left)
    tags = "#" * int(left)
    spaces = " " * int(right)
    percents = "{:.0%}". format(percent)
    print("\r[", tags, spaces, "] ", percents, sep="", end="", flush=True)

the_list = ['a', 'b', 'c', 1, 2, 3, 3.14, (1010, 'a')]
df = pd.DataFrame(the_list)

print("Progress bar iterating a list")
for i, j in enumerate(the_list):
    progress_bar(i+1, 100, len(the_list))
    sleep(0.2)
print("\nProgress bar iterating a dataframe")
for index, row in df.iterrows():
    progress_bar(index+1, 100, len(df.index))
    sleep(0.2)