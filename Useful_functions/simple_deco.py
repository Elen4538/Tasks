from functools import wraps


def makeDecorator(old_dec):
  
    def wrapper(func): 
      @wraps
        def inner(*ar, **kw):
            return old_dec(func, *ar, **kw)
        return inner
    return wrapper
  
  
