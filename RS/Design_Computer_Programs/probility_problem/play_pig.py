# -----------------
# User Instructions
#
# Write the two action functions, hold and roll. Each should take a
# state as input, apply the appropriate action, and return a new
# state.
#
# States are represented as a tuple of (p, me, you, pending) where
# p:       an int, 0 or 1, indicating which player's turn it is.
# me:      an int, the player-to-move's current score
# you:     an int, the other player's current score.
# pending: an int, the number of points accumulated on current turn, not yet scored

from collections import namedtuple
# 练习使用 namedtuple
State = namedtuple('state', "p me you pending")
s = State(1, 2, 3, 4)
# print(s.p)
# print(s.me)
# print(s.you)
# print(s.pending)


def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    # your code here
    p, me, you, pending = state
    # if p == 0:
    #     return (1 , you, pending + me, 0)
    # else:
    #     return (0, you, pending + me, 0)
    return (other_turn[p], you, pending + me, 0)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    # your code here
    p, me, you, pending = state
    if d is 1:
        return (other_turn[p], you, me+1, 0 )
    else:
        return (p, me, you, pending + d)

other_turn = {0:1, 1:0}

def test():
    assert hold((1, 10, 20, 7)) == (0, 20, 17, 0)
    assert hold((0, 5, 15, 10)) == (1, 15, 15, 0)
    assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
    assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
    return 'tests pass'


print(test())

# -----------------
# User Instructions
#
# Write a strategy function, clueless, that ignores the state and
# chooses at random from the possible moves (it should either
# return 'roll' or 'hold'). Take a look at the random library for
# helpful functions.

import random

possible_moves = ['roll', 'hold']

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    # your code here
    # select = random.randint(0, 1)
    # return possible_moves[select]
    return random.choice(possible_moves)


# -----------------
# User Instructions
#
# In this problem, you will complete the code for the hold_at(x)
# function. This function returns a strategy function (note that
# hold_at is NOT the strategy function itself). The returned
# strategy should hold if and only if pending >= x or if the
# player has reached the goal.

def hold_at(x):
    """Return a strategy that holds if and only if
    pending >= x or player reaches goal."""

    def strategy(state):
    # your code here
        p, me, you, pending = state
        return "hold" if (pending >= x or me + pending >= goal) else "roll"
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy


goal = 50


def test1():
    assert hold_at(30)((1, 29, 15, 20)) == 'roll'
    assert hold_at(30)((1, 29, 15, 21)) == 'hold'
    assert hold_at(15)((0, 2, 30, 10)) == 'roll'
    assert hold_at(15)((0, 2, 30, 15)) == 'hold'
    return 'tests pass'


print(test1())


def play_pig(A, B):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    # your code here
    strategies = [A,B]
    state = (0,0,0,0)
    while True:
        p, me, you, pending = state
        if me >= goal:
            return strategies[p]
        elif you >= goal:
            return strategies[other_turn[p]]
        elif strategies[p](state) == 'hold':
            state = hold(state)
        else:
            state = roll(state, random.randint(1,6))


def always_roll(state):
    return 'roll'


def always_hold(state):
    return 'hold'


def test2():
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
    return 'tests1 pass'


print(test2())
# -----------------
# User Instructions
#
# Write the max_wins function. You can make your life easier by writing
# it in terms of one or more of the functions that we've defined! Go
# to line 88 to enter your code.

from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

# 通过质量函数和效用函数找到最好的执行Action
goal = 40
def Q_pig(state, action, Pwin):
    "The expect value of choosing action in state"
    if action is "hold":
        return 1 - Pwin(hold(state))
    if action is "roll":
        return (1-Pwin(roll(state,1)) +
                sum(Pwin(roll(state, a)) for a in (2, 3, 4, 5, 6))) / 6.
    raise ValueError


def pig_actions(state):
    "The Legal actions from a state."
    _,_,_,pending = state
    return ["hold","roll"] if pending else ["roll"]

def best_action(state):
    "Return the optimal action for a state , give U."
    def EU(action): return Q_pig(state, action, Pwin)
    return max(pig_actions(state),key=EU)

#包含递归要优化
@memo
def Pwin(state):
    """The utility of a state, here just the probability that an optimal player whose turn it
     to move can win from the current state"""
    # Assumes opponent also plays with optimal strategy
    p, me, you, pending = state
    if me + pending >= goal:
        return 1
    elif you >= goal:
        return 0
    else:
        return max(Q_pig(state, action, Pwin) for action in pig_actions(state))

def max_wins(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state)# your code here


def test3():
    assert(max_wins((1, 5, 34, 4)))   == "roll"
    assert(max_wins((1, 18, 27, 8)))  == "roll"
    assert(max_wins((0, 23, 8, 8)))   == "roll"
    assert(max_wins((0, 31, 22, 9)))  == "hold"
    assert(max_wins((1, 11, 13, 21))) == "roll"
    assert(max_wins((1, 33, 16, 6)))  == "roll"
    assert(max_wins((1, 12, 17, 27))) == "roll"
    assert(max_wins((1, 9, 32, 5)))   == "roll"
    assert(max_wins((0, 28, 27, 5)))  == "roll"
    assert(max_wins((1, 7, 26, 34)))  == "hold"
    assert(max_wins((1, 20, 29, 17))) == "roll"
    assert(max_wins((0, 34, 23, 7)))  == "hold"
    assert(max_wins((0, 30, 23, 11))) == "hold"
    assert(max_wins((0, 22, 36, 6)))  == "roll"
    assert(max_wins((0, 21, 38, 12))) == "roll"
    assert(max_wins((0, 1, 13, 21)))  == "roll"
    assert(max_wins((0, 11, 25, 14))) == "roll"
    assert(max_wins((0, 22, 4, 7)))   == "roll"
    assert(max_wins((1, 28, 3, 2)))   == "roll"
    assert(max_wins((0, 11, 0, 24)))  == "roll"
    return 'tests3 pass'

print(test3())

