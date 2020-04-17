from functools import update_wrapper
#重构方法 使接受两个参数的方法能接受多个参数
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    update_wrapper(n_ary_f,f)
    return n_ary_f

# 装饰器
@ n_ary
def seq(x,y): return ('seq', x, y)

