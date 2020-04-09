import math
def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
def all_ints():
    yield 0
    i = 1
    while i < 100:
        yield +i
        yield -i
        i = i + 1


# a = (v for v in all_ints ())

print(next(ints(0, 100)),next(ints(0, 100)),next(ints(0, 100)) )
# print(next(a),next(a),next(a) )
print([v for v in all_ints()])