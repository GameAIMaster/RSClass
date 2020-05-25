from Design_Computer_Programs.tools.MathLanguage import *
# parse/convert str regular expression to API

def star(x): return lambda t: (set([t]) |
                               set(t2 for t1 in x(t) if t1 != t
                                   for t2 in star(x)(t1)))

REGRAMMAR = grammar("""
eol => $
dot => [.]
lit => \w
lits => lit lits | lit
oneof => [[] lits []]
RE1 => group | oneof | lit | dot
opt => RE1 [?] 
plus => RE1 [+] 
star => RE1 [*] 
staropt => RE1 [*][?]
optstar => RE1 [?][*]
optplus => RE1 [?][+]
plusopt => RE1 [+][?]
RE2 => staropt | optstar | plusopt | optplus | opt | plus | star | RE1
seq => RE2 seq | RE2
alt => seq [|] alt | seq
RE => alt
group => [(] RE [)]
""", whitespace=" ")

def parse_re(pattern):
        return convert(parse('RE', pattern, REGRAMMAR))

def convert(tree):
    "Convert a REGRAMMAR parse tree into our regex (compiler) API"
    root = tree[0]
    names = {
        'optplus': 'plus(opt({x}))',
        'plusopt': 'opt(plus({x}))',
        'staropt': 'opt(star({x}))',
        'optstar': 'star(opt({x}))',
    }
    if isinstance(tree, list):
        try:
            if root in ('plus', 'star', 'opt', 'lit'):
                return '{r}({x})'.format(r=root, x=convert(tree[1]))
            elif root in ('optplus', 'plusopt', 'staropt', 'optstar'):
                return names[root].format(x=convert(tree[1]))
            elif root == 'oneof':
                return 'oneof({x})'.format(x=convert(tree[2]))
            elif root == 'group':
                return convert(tree[2])
            elif root == 'alt':
                if len(tree) == 2:
                    return convert(tree[1])
                else:
                    return 'alt({a}, {b})'.format(a=convert(tree[1]),
                                                  b=convert(tree[3]))
            elif root in ('seq', 'lits'):
                if len(tree) == 2:
                    return convert(tree[1])
                else:
                    return 'seq({a})'.format(a=', '.join(map(convert, tree[1:])))
            else:
                return convert(tree[1])
        except Exception as err:
            print('tree: {t}'.format(t=tree))
            raise
    else:
        return repr(tree)

fail = (None, None)



