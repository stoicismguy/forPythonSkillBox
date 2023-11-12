import time
memoize_dict = dict()


def validate_args(func):
    def wrapped(*args, **kwargs):
        if len(args) + len(kwargs) < 1:
            return "Not enough arguments"
        if len(args) + len(kwargs) > 1:
            return "Too many arguments"
        else:
            if not isinstance(args[0], int):
                return "Wrong types"
            if args[0] < 0:
                return "Negative argument"
        return func(*args, **kwargs)
    return wrapped


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


def timer(func):
    def wrapped(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} сработала за", end - start)
        return result
    return wrapped


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@memoize
def fibonacci_w_memoizer(n):
    if n < 2:
        return n
    return fibonacci_w_memoizer(n - 1) + fibonacci_w_memoizer(n - 2)


@validate_args
@timer
def temporar(n):
    return fibonacci(n)

@validate_args
@timer
def temporar_w_memoizer(n):
    return fibonacci_w_memoizer(n)

n = 36
print(temporar(n))
print(temporar_w_memoizer(n))
