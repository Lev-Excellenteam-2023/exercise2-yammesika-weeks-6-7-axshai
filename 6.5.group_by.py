

def group_by(func, iterable):
    """
     Groups the elements of an iterable based on a given function.
    :param func: The function used to group the elements of the iterable.
    :param iterable: The iterable to be grouped.
    :return: A dictionary where the keys are the results of applying `func` to the elements of `iterable`,
            and the values are lists of the elements that have that key.
    """
    grouped_dict = {func(i): [] for i in iterable}
    [grouped_dict[func(i)].append(i) for i in iterable]
    return grouped_dict
