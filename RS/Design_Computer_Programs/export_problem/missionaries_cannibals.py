import operator
# -----------------
# User Instructions
#
# Write a function, csuccessors, that takes a state (as defined below)
# as input and returns a dictionary of {state:action} pairs.
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings:
#
# 'MM->', 'MC->', '<-CC', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C', '<-CC'
# where 'MM->' means two missionaries travel to the right side.
#
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    # your code here
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    items = []
    if B1 > 0:
        items += [(add(state, item), a+'->') for item, a in delta.items() if item[0]+state[0] >=0 and item[1]+state[1] >= 0]
    if B2 > 0:
        items += [(sub(state, item), '<-'+a) for item, a in delta.items() if state[3] - item[3] >= 0 and state[4] - item[4] >= 0]

    return dict(items)
delta = {(0, -1, -1,      0, 1, 1): 'C',
        (-1, 0, -1,       1, 0, 1): 'M',
        (-2, 0, -1,       2, 0, 1): 'MM',
        (-1, -1, -1,       1, 1, 1): 'MC',
        (0, -2, -1,       0, 2, 1): 'CC'}
    # if B1 is 1:
    #     result = {(M1, C1-1, 0, M2, C2+1, 1):'C->',
    #             (M1-1, C1, 0, M2+1, C2, 1):'M->',
    #             (M1-2, C1, 0, M2+2, C2, 1):'MM->',
    #             (M1-1, C1-1, 0, M2+1, C2+1, 1):'MC->',
    #             (M1, C1-2, 0, M2, C2+2, 1):'CC->'}
    #     removek = []
    #     for k,v in result.items():
    #         m1, c1, b1, m2, c2, b2 = k
    #         if m1<0 or c1 < 0 :
    #             removek.append(k)
    #     for k in removek:
    #         result.pop(k)
    #     return result
    # else:
    #     result = {(M1, C1 + 1, 1, M2, C2 - 1, 0): '<-C',
    #             (M1 + 1, C1, 1, M2 - 1, C2, 0): '<-M',
    #             (M1 + 2, C1, 1, M2 - 2, C2, 0): '<-MM',
    #             (M1 + 1, C1 + 1, 1, M2 - 1, C2 - 1, 0): '<-MC',
    #             (M1, C1 + 2, 1, M2, C2 - 2, 0): '<-CC'}
    #     removek=[]
    #     for k,v in result.items():
    #         m1, c1, b1, m2, c2, b2 = k
    #         if m2<0 or c2 < 0:
    #             removek.append(k)
    #     for k in removek:
    #         result.pop(k)
    #     return result
def add(a, b):
    #两个矩阵相加
    return tuple(x+y for x,y in zip(a,b))

def sub(a, b):
    #两个矩阵相减
    return tuple(x-y for x,y in zip(a,b))


def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                               (2, 1, 1, 3, 3, 0): '<-M',
                                               (3, 1, 1, 2, 3, 0): '<-MM',
                                               (1, 3, 1, 4, 1, 0): '<-CC',
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 1, 0, 1, 1, 1)) == {(1, 2, 1, 1, 0, 0): '<-C',
                                               (2, 1, 1, 0, 1, 0): '<-M',
                                               (2, 2, 1, 0, 0, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print(csuccessors((1, 1, 0, 1, 1, 1)))
print(test())
# print(csuccessors((1, 1, 0, 1, 1, 1)))

def mc_problem(start=(0, 0), goal=None):
    """"""
    if goal is None:
        goal = (0, 0, 0) + start[:3]
    if goal in start:
        return [start]
    export = set() # set of states we have visited
    frontier = [ [start] ] # orderd list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in csuccessors(s).items():
            if state not in export:
                export.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []


def is_goal(state):
    if state == 5:
        return True
    else:
        return False


#最短路径问题抽象
# -----------------
# User Instructions
#
# Write a function, shortest_path_search, that generalizes the search algorithm
# that we have been using. This function should have three inputs, a start state,
# a successors function, and an is_goal function.
#
# You can use the solution to mc_problem as a template for constructing your
# shortest_path_search. You can also see the example is_goal and successors
# functions for a simple test problem below.
def successors(state):
    successors = {state + 1: '->',
                  state - 1: '<-'}
    return successors

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    # your code here
    if is_goal(start):
        return [start]
    export = set() # set of states we have visited
    frontier = [ [start] ] # orderd list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in export:
                export.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail
# test
assert shortest_path_search(5, successors, is_goal) == [5]
print(shortest_path_search(5, successors, is_goal))


# -----------------
# User Instructions
#
# Write a function, mc_problem2, that solves the missionary and cannibal
# problem by making a call to shortest_path_search. Add any code below
# and change the arguments in the return statement's call to the
# shortest_path_search function
def mc_problem2(start=(3, 3, 1, 0, 0, 0), goal=None):
    # your code here if necessary
    if goal is None:
        def goal_fn(state):
            return state[:3] == (0, 0, 0)
    else:
        def goal_fn(state): #定义好目标
            return state == goal
    return shortest_path_search(start, csuccessors, goal_fn)

def test():
    assert mc_problem2(start=(1, 1, 1, 0, 0, 0)) == [
                             (1, 1, 1, 0, 0, 0), 'MC->',
                             (0, 0, 0, 1, 1, 1)]
    assert mc_problem2() == [(3, 3, 1, 0, 0, 0), 'CC->',
                             (3, 1, 0, 0, 2, 1), '<-C',
                             (3, 2, 1, 0, 1, 0), 'CC->',
                             (3, 0, 0, 0, 3, 1), '<-C',
                             (3, 1, 1, 0, 2, 0), 'MM->',
                             (1, 1, 0, 2, 2, 1), '<-MC',
                             (2, 2, 1, 1, 1, 0), 'MM->',
                             (0, 2, 0, 3, 1, 1), '<-C',
                             (0, 3, 1, 3, 0, 0), 'CC->',
                             (0, 1, 0, 3, 2, 1), '<-C',
                             (0, 2, 1, 3, 1, 0), 'CC->',
                             (0, 0, 0, 3, 3, 1)]
    return 'tests pass'

print(mc_problem2() )