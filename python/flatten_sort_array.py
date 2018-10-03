def flatten_and_sort(array):
    return sorted(list([item for sublist in array for item in sublist]))