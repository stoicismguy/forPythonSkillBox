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
