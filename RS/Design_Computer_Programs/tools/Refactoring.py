from functools import update_wrapper
#重构方法 使接受两个参数的方法能接受多个参数 表达工具

def decorator(d):
    "Make function d a decorator: d weaps a function fn."
    "n_aray -> decorator(n_aray) seq->fn 执行了 update_wrapper(n_aray(seq)==>n_nary_f, seq) 有些难懂"
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    # update_wrapper(n_ary_f,f)
    return n_ary_f

# 装饰器
@ n_ary
def seq(x,y): return ('seq', x, y)

# 用来查找语法中的错误，
def verify(G):
    lhstokens = set(G) - set([' '])
    rhstokens = set(t for alts in G.values() for alt in alts for t in alt)
    def show(title, tokens): print (title,'=',' '.join(sorted(tokens)))
    show('None-Terms', G)
    show('Terminals ', rhstokens - lhstokens)
    show('Suspects  ', [t for t in (rhstokens - lhstokens) if t.isalnum()]) # 找到因该出现在左边的token
    show('Orphans   ', lhstokens - rhstokens)
# print(seq('a','b','c'))




