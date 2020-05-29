"""有一个农夫带一只羊、一筐菜和一只狼过河，如果没有农夫看管，
则狼要吃羊，羊要吃菜，但是船很小，只够农夫带一样东西过河。
问农夫该如何解此难题？
解：state包含河there,here两边的状态,there:frozenset(['farmer','sheep','wolf','vegetables','ship'] action:(1,2,'->')"""
# from Design_Computer_Programs.tools.MathLanguage import *
def csuccessor(state):
    there, here = state
    if 'farmer' in there and 'ship' in there:
        return dict((there - frozenset(['farmer',a,'ship']),
                      here | frozenset(['farmer',a,'ship']))
                      for a in there if a is not 'ship' and
                    ('wolf' not in (there - a) and 'sheep' not in (there - a)) or
                    ('vegetables' not in (there - a) and 'sheep' not in (there - a)))
    else:
        return dict((here - frozenset(['farmer', a, 'ship']),
                     there | frozenset(['farmer', a, 'ship']))
                    for a in here if a is not 'ship' and
                    ('wolf' not in (there - a) and 'sheep' not in (there - a)) or
                    ('vegetables' not in (there - a) and 'sheep' not in (there - a))
                    )

def cross_river(goal, start=(frozenset(['farmer','sheep','wolf','vegetables','ship']), frozenset([]))):
    if goal in start:
        return [start]
    export = set() # set of states we have visited
    frontier = [ [start] ] # orderd list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1]
        for (state, action) in csuccessor().items():
            if state not in export:
                export.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

cross_river((frozenset([]),))
