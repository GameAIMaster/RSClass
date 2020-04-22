import math
# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the
# non-negative numbers. The runtime of your program should be
# proportional to the LOGARITHM of the input. You may want to
# do some research into binary search and Newton's method to
# help you out.
#
# This function should return another function which computes the
# inverse of the input function.
#
# Your inverse function should also take an optional parameter,
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is
# efficient enough.

def slow_inverse(f, delta=1 / 128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""

    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x) - y < y - f(x - delta)) else x - delta

    return f_1


def fast_inverse(f, delta=1 / 1024.):
    def f_1(y):
        lo, hi = find_bounds(f, y)
        print (lo, hi)
        return binary_search(f, y, lo, hi, delta)
    return f_1

def find_bounds(f, y):
    # 通过x主键翻倍锁定x的范围，在毫无信息的时候二倍法是最有效的确定范围
    x = 1.
    while f(x) < y:
        x = x * 2
    lo = 0 if (x == 1) else x/2
    return lo, x

def binary_search(f, y, lo, hi, delta):
    # 二分法在范围内查很早很有效
    "Given f(lo) <= y <= f(hi) ,return x such that f(x) is within delta of y"
    while lo < hi:
        medium = (hi + lo) / 2
        if(f(medium) > y ):
            hi = medium - delta
        elif(f(medium) < y):
            lo = medium + delta
        else:
            return medium

    print("stop")
    return hi if (f(lo)-y > f(hi) - y) else lo




@slow_inverse
def inverse(f, delta=1 / 1024.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""


def square(x): return x * x
def power10(x): return 10 ** x


sqrt = fast_inverse(square)
log10 = fast_inverse(power10)
cuberoot = fast_inverse(lambda  x: x*x*x)
print(sqrt(10000000000))
def test():
    nums = [2, 4, 6, 8, 10, 99, 100, 101, 1000, 10000, 20000, 40000, 100000000]
    for n in nums:
        test1(n, 'sqrt', sqrt(n), math.sqrt(n))
        test1(n, 'log', log10(n), math.log10(n))
        test1(n, '3-rt', cuberoot(n), n**(1./3.))

def test1(n, name, value, expected):
    diff = abs(value-expected)
    print('%6g: %s = %12.7f (%3.7f actual); %.4f diff; %s' % (
        n, name, value, expected, diff,('ok' if diff < 0.002 else '*****BAD*****')))

test()
