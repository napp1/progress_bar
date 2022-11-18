# Progress Bar for List and Dataframe iteration

**progress_bar** is a short and simple function that print a progress bar.

It accepts 3 parameters:

- current_element - current position in list or df during the iteration (int)
- bar_width - the width of the progress bar in number of characters (int)
- list_length - the length of the list or df to iterate (int)

I wrote it to have an easy way to integrate a progress bar into the iteration of a list or a Pandas DataFrame.

The function was inspired by this post: https://www.codingem.com/progress-bar-in-python/

## Usage in a list iteration

```
for i, j in enumerate(the_list):
    progress_bar(i+1, 100, len(the_list))
```
## Usage in a DataFrame iteration

```
for index, row in df.iterrows():
    progress_bar(index+1, 100, len(df.index))