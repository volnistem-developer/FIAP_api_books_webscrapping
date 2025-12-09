def protected():
    def wrapper(func):
        setattr(func, "_protected", True)
        return func
    
    return wrapper