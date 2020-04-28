def pour_problem(X, Y, goal, start=(0, 0)):
    """X and Y are the capacity of glasses; (x, y) is current fill levels
    and represents a state. The goal is a level that can be in either glass.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored ; fail when no frontier."""
    if goal in start:
        return [start]
    export = set() # set of states we have visited
    frontier = [ [start] ] # orderd list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1]
        for (state, action) in successor(x, y, X, Y).items():
            if state not in export:
                export.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

def successor(x, y, X, Y):
    """return a dict of {state:action} pairs describing what can be reached from the (x, y) state, and how """
    assert x <= X and y <= Y ## (x,y) is glass levels; X and Y are glass size
    return {((0, y+x) if y+x <= Y else (x-(Y-y), y+(Y-y))): "x->y",
            ((x+y, 0) if x+y <= X else (x+(X-x), y-(X-x))): "x<-y",
            (X, y): "fill X", (x, Y): "fill Y",
            (0, y): "empty X", (x, 0): "empty Y"}

# print(pour_problem(9, 4, 7))
# print(successor( 0,0,9, 4))

import doctest
class Test:"""
>>> successor(0, 0, 9, 4)
{(0, 0): 'empty Y', (9, 0): 'fill X', (0, 4): 'fill Y'}
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)