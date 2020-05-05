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
print(s.p)
print(s.me)
print(s.you)
print(s.pending)


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

    strategy.__name__ = 'hold_at(%d)' % x
    return strategy


goal = 50


def test():
    assert hold_at(30)((1, 29, 15, 20)) == 'roll'
    assert hold_at(30)((1, 29, 15, 21)) == 'hold'
    assert hold_at(15)((0, 2, 30, 10)) == 'roll'
    assert hold_at(15)((0, 2, 30, 15)) == 'hold'
    return 'tests pass'


print(test())