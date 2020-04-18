from Design_Computer_Programs.tools.Refactoring import *
# 缓存技术 if n in cache return cache[n]
@decorator
def memo(f):
    cache = {}
    def _f(*args):
        """ Decorator that caches the return value for each call to f(args).
        Then when called again with same args, we can just look it up"""
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)

print(seq('a','b','c'))