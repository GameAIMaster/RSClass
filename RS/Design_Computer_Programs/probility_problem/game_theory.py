million = 1000000

def Q(state, action, U):
    "the expected value of taking action instate, according to utility U"
    if action == 'hold':
        return U(state + 1*million)
    if action == "gamble":
        return U(state + 3*million)*.5 + U(state) * .5

def actions(state): return ["hold", 'gamble']

def identity(x): return x

U = identity

def best_action(state):
    "Return the optimal action for a state , give U."
    def EU(action): return Q(state, action, U)
    return max(actions(state),key=EU)