memoize_dict = dict()
def memoize(func):
    global memoize_dict

    def wrapped(*args):
        if func.__name__ in memoize_dict.keys():
            if args[0] in memoize_dict[func.__name__].keys():
                return memoize_dict[func.__name__][args[0]]
            else:
                f = func(*args)
                memoize_dict[func.__name__][args[0]] = f
                return f
        else:
            memoize_dict[func.__name__] = dict()
            return wrapped(*args)

    return wrapped


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
