

def group_by(func, iterable):
    """
     Groups the elements of an iterable based on a given function.
    :param func: The function used to group the elements of the iterable.
    :param iterable: The iterable to be grouped.
    :return: A dictionary where the keys are the results of applying `func` to the elements of `iterable`,
            and the values are lists of the elements that have that key.
    """
    grouped_dict = {func(item): [] for item in iterable}
    for item in iterable:
        grouped_dict[func(item)].append(item)
    return grouped_dict


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
