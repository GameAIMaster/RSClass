import doctest
# from Design_Computer_Programs.tools.Memoization import *  #用来计算执行时间
# -----------------
# User Instructions
#
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is
# '->' for here to there or '<-' for there to here. When only one
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state
    # your code here
    # return {(there.remove(x,'light'),here.add(x,'light')):(x for x in there, x for x in there,'->'),
    # (here.remove(x,'light'),there.add(x,'light')):(x for x in there, x for x in there,'<-'),
    # }
    if 'light' in there:
        return dict(((here | frozenset([a, b, 'light']),
                    there - frozenset([a, b, 'light']),
                                      t + max(a, b)),
                                      (a, b, '<-'))
                                      for a in there if a is not 'light'
                                      for b in there if b is not 'light')
    else:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light']),
                                       t + max(a, b)),
                    (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')


def test():
    print( bsuccessors((frozenset([1, 'light']), frozenset([]), 3))) == {
        (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) == {
        (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    return 'tests pass'


print(test())

# User Instructions
#
# Write two functions, path_states and path_actions. Each of these
# functions should take a path as input. Remember that a path is a
# list of [state, action, state, action, ... ]
#
# path_states should return a list of the states. in a path, and
# path_actions should return a list of the actions.

def path_states(path):
    "Return a list of states in this path."
    # return [state for i, state in enumerate(path) if i % 2 == 0]
    return path[0::2]
def path_actions(path):
    "Return a list of actions in this path."
    # return [action for i,action in enumerate(path) if i % 2 == 1]
    return path[1::2]
def test1():
    testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
                (5, 2, '->'),                                        # action 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
                (2, 1, '->'),                                        # action 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (5, 5, '->'),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (5, 10, '->'),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (2, 2, '->'),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (10, 1, '->'),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (10, 10, '->'),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (10, 2, '->'),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (5, 1, '->'),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
                (1, 1, '->')]
    assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
    assert path_actions(testpath) == [(5, 2, '->'), # action 1
                                      (2, 1, '->'), # action 2
                                      (5, 5, '->'),
                                      (5, 10, '->'),
                                      (2, 2, '->'),
                                      (10, 1, '->'),
                                      (10, 10, '->'),
                                      (10, 2, '->'),
                                      (5, 1, '->'),
                                      (1, 1, '->')]
    return 'tests pass'

# print(test1())


def elapsed_time(path):
    return path[-1][2]
# @timecalls
def bridge_problem(here):
    """Modify this to test for goal later: after pulling a state off frontier,
    not when we are about to put it on the frontier."""
    ## modify code below
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)
        here1, there1, t1 = state1 = path[-1]
        if not here1 or here1 == set('light'):
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                # if not here:  ## That is, nobody left here
                #     return path2
                # else:
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
    return []

def test2():
    assert bridge_problem(frozenset((1, 2),))[-1][-1] == 2 # the [-1][-1] grabs the total elapsed time
    assert bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1] == 17
    return 'tests pass'

# print(test2())

# class TestBridge: """
# >>> elapsed_time(bridge_problem2([1,2,5,10]))
# 17
#
# ## There are two equally good solutions
# >>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
# >>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
# >>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
# True
#
# ## Try some other problems
# >>> path_actions(bridge_problem([1,2,5,10,15,20]))
# [(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]
#
# >>> path_actions(bridge_problem([1,2,4,8,16,32]))
# [(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]
#
# >>> path_actions(bridge_problem([1,2,4,8,16]))
# [(2, 1, '->'), (1, 1, '<-'), (8, 16, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (4, 1, '->')]
#
# >>> [elapsed_time(bridge_problem([1,2,4,8,16][:N])) for N in range(6)]
# [0, 1, 2, 7, 15, 28]
#
# >>> path_actions(bridge_problem([1,1,2,3,5,8,13,21]))
# [(2, 1, '->'), (1, 1, '<-'), (8, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (13, 21, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (3, 1, '->')]
#
# >>> [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(8)]
# [0, 1, 1, 2, 6, 12, 19, 30]
#
# >>> path_actions(bridge_problem([]))
# []
# """

# print(doctest.testmod())
# print([(elapsed_time(bridge_problem([1,2,4,8,16][0:6])),N) for N in range(0,5)])

def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    # your code here
    here, there = state
    if 'light' in here:
        return dict(((here - frozenset([a,b, 'light']),
                      there | frozenset([a, b, 'light'])),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a,b, 'light']),
                      there - frozenset([a, b, 'light'])),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')


def test3():
    here1 = frozenset([1, 'light'])
    there1 = frozenset([])

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])

    assert bsuccessors2((here1, there1)) == {
        (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}
    assert bsuccessors2((here2, there2)) == {
        (frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'),
        (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'),
        (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}
    return 'tests pass'


# print(test3())


# -----------------
# User Instructions
#
# Write a function, path_cost, which takes a path as input
# and returns the total cost associated with that path.
# Remember that paths will obey the convention
# path = (state, (action, total_cost), state, ...)
#
# If a path is less than length 3, your function should
# return a cost of 0.

def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = (state, (action, total_cost), state, ... )
    if len(path) < 3:
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost


# ???

def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem."""
    # An action is an (a, b, arrow) tuple; a and b are
    # times; arrow is a string.
    a, b, arrow = action
    return max(a, b)


def test4():
    assert path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2')) == 5
    assert path_cost(('fs1', ((2, 1, '->'), 2), 'fs2', ((3, 4, '<-'), 6), 'fs3')) == 6
    assert bcost((4, 2, '->'), ) == 4
    assert bcost((3, 10, '<-'), ) == 10
    return 'tests pass'

# print(test4())

# @timecalls
def bridge_problem2(here):
    """Modify this to test for goal later: after pulling a state off frontier,
    not when we are about to put it on the frontier."""
    ## modify code below
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [ [(here, frozenset())] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        here1, there1 = state1 = final_state(path)
        if not here1 or here1 == set('light'):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in bsuccessors2(state1).items():
            if state not in explored:
                path2 = path + [(action, pcost+bcost(action)), state]
                add_to_frontier(frontier, path2)

    return []

def final_state(path): return path[-1]

def add_to_frontier(frontier, path):
    "Add path to frontier, replacing costlier path if there is one."
    #(This could be done mor efficiently.)
    # Find if there is an old path to the final state of this path.
    old = None
    for i,p in enumerate(frontier):
        if (final_state(p) == final_state(path)):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return # Old path was better; do nothing
    elif old is not None:
        del frontier[old] # Old path was worse; delete it
    ## Now add the new path and re-sort
    frontier.append(path)
    frontier.sort(key=path_cost) # sort还能利用树结构进行优化

# bridge_problem([1,1,2,3,5,8,13,21])
# bridge_problem2([1,1,2,3,5,8,13,21])
# print('bridge_problem计算用时：%s' % (timefun[bridge_problem]))
# print('bridge_problem2计算用时：%s' % (timefun[bridge_problem2]))


# --------------
# Example problem
#
# Let's say the states in an optimization problem are given by integers.
# From a state, i, the only possible successors are i+1 and i-1. Given
# a starting integer, find the shortest path to the integer 8.
#
# This is an overly simple example of when we can use the
# shortest_path_search function. We just need to define the appropriate
# is_goal and successors functions.


# -----------------
# User Instructions
#
# Define a function, lowest_cost_search, that is similar to
# shortest_path_search, but also takes into account the cost
# of an action, as defined by the function action_cost(action)
#
# Since we are using this function as a generalized version
# of the bridge problem, all the code necessary to solve that
# problem is included below for your reference.
#
# This code will not run yet. Click submit to see if your code
# is correct.


def lowest_cost_search(start, successors, is_goal, action_cost):
    """Return the lowest cost path, starting from start state,
    and considering successors(state) => {state:action,...},
    that ends in a state for which is_goal(state) is true,
    where the cost of a path is the sum of action costs,
    which are given by action_cost(action)."""
    # your code here
    export = set()  # set of states we have visited
    frontier = [[start]]  # orderd list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        state1 = final_state(path)
        if is_goal(state1):
            return path
        export.add(state1)
        pcost = path_cost(path)
        for (state, action) in successors(state1).items():
            if state not in export:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail

Fail = []

# -----------------
# User Instructions
#
# In this problem, you will generalize the bridge problem
# by writing a function bridge_problem3, that makes a call
# to lowest_cost_search.

def bridge_problem3(here):
    """Find the fastest (least elapsed time) path to
    the goal in the bridge problem."""
    # your code here
    here = frozenset(here) | frozenset(['light'])
    # State will be a (people-here, people-there, time-elapsed)
    start = (here, frozenset())  # ordered list of paths we have blazed
    return lowest_cost_search(start, bsuccessors2, all_over, bcost) # <== your arguments here


def all_over(state):
    here, there = state
    return not here or here == set(['light'])
# your code here if necessary

def test5():
    here = [1, 2, 5, 10]
    assert bridge_problem3(here) == [
            (frozenset([1, 2, 'light', 10, 5]), frozenset([])),
            ((2, 1, '->'), 2),
            (frozenset([10, 5]), frozenset([1, 2, 'light'])),
            ((2, 2, '<-'), 4),
            (frozenset(['light', 10, 2, 5]), frozenset([1])),
            ((5, 10, '->'), 14),
            (frozenset([2]), frozenset([1, 10, 5, 'light'])),
            ((1, 1, '<-'), 15),
            (frozenset([1, 2, 'light']), frozenset([10, 5])),
            ((2, 1, '->'), 17),
            (frozenset([]), frozenset([1, 10, 2, 5, 'light']))]
    return 'test5 passes'

print(test5())



# User Instructions
#
# In this problem you will be refactoring the bsuccessors function.
# Your new function, bsuccessors3, will take a state as an input
# and return a dict of {state:action} pairs.
#
# A state is a (here, there, light) tuple. Here and there are
# frozensets of people (each person is represented by an integer
# which corresponds to their travel time), and light is 0 if
# it is on the `here` side and 1 if it is on the `there` side.
#
# An action is a tuple of (travelers, arrow), where the arrow is
# '->' or '<-'. See the test() function below for some examples
# of what your function's input and output should look like.

def bsuccessors3(state):
    """Return a dict of {state:action} pairs.  State is (here, there, light)
    where here and there are frozen sets of people, light is 0 if the light is
    on the here side and 1 if it is on the there side.
    Action is a tuple (travelers, arrow) where arrow is '->' or '<-'"""
    _, _, light = state
    return dict(bsuccessor3(state, set([a, b]))
                for a in state[light]
                for b in state[light])

def bsuccessor3(state, travels):
    """The single successors state when this set of travels move"""
    _, _, light = state
    start = state[light] - travels
    desk = state[1 - light ] | travels
    if light == 0:
        return (start, desk, 1), (travels, '->')
    else:
        return (desk, start, 0), (travels, '<-')

def test6():
    print(bsuccessors3((frozenset([1]), frozenset([]), 0)))
    assert bsuccessors3((frozenset([1]), frozenset([]), 0)) == {
            (frozenset([]), frozenset([1]), 1)  :  (set([1]), '->')}

    assert bsuccessors3((frozenset([1, 2]), frozenset([]), 0)) == {
            (frozenset([1]), frozenset([2]), 1)    :  (set([2]), '->'),
            (frozenset([]), frozenset([1, 2]), 1)  :  (set([1, 2]), '->'),
            (frozenset([2]), frozenset([1]), 1)    :  (set([1]), '->')}

    assert bsuccessors3((frozenset([2, 4]), frozenset([3, 5]), 1)) == {
            (frozenset([2, 4, 5]), frozenset([3]), 0)   :  (set([5]), '<-'),
            (frozenset([2, 3, 4, 5]), frozenset([]), 0) :  (set([3, 5]), '<-'),
            (frozenset([2, 3, 4]), frozenset([5]), 0)   :  (set([3]), '<-')}
    return 'tests6 pass'

print(test6())