def validate_length(func):
    def wrapper(length, *args, **kwargs):
        if length < 6:
            raise ValueError("Password length must be at least 6.")
        return func(length, *args, **kwargs)
    return wrapper
