from Design_Computer_Programs.tools.Refactoring import *
# 缓存技术 if n in cache return cache[n] 性能工具
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
            return f(*args)
    return _f

# 调用计数 调试工具
@decorator
def countcalls(f):
    """ Decorator that makes the function count calls to it, in callcounts[f]."""
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}


#trace 调试工具
@decorator
def trace(f):
    indent = '  '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print('%s--> %s' % (trace.level*indent, signature))
        trace.level += 1
        # 保证遇到错误也能返回
        try:
            result = f(*args)
            print('%s<-- %s == %s' % ((trace.level-1)*indent,
                                      signature, result))
        finally:
            trace.level -= 1
            return result

    trace.level = 0
    return _f

def disable(f): return f
trace=disable
# @countcalls
# @memo

@trace
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

# 测试调用计数
# print("n     fib(n)     calls     callratio")
# # old = 1
# for i in range(22):
#     callcounts[fib] = 0
#     print("%d     %d     %d     %f" % (i, fib(i), callcounts[fib], fib(i)/fib(i - 1)))






fib(6) #running this in the browser's IDE  will not display the indentations!





