import time


def timer(func, *args, **kargs):
    """
    Measures the execution time of a function and returns the elapsed time in seconds.
    :param func: The function to measure the execution time of
    :param args: The positional arguments to pass to the input function.
    :param kargs: The keyword arguments to pass to the input function.
    :return:    The elapsed time in seconds.
    """
    start_time = time.time()
    func(*args, **kargs)
    end_time = time.time()

    return end_time - start_time


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
