from Design_Computer_Programs.tools.MathLanguage import *
findtag = '(Write\w+[(]\s*((\w+.)*[^"]+,)*\s*stream)'
PACKETGRAMMAR = grammar("""
write    => Write Type ( args stream
args     => arg , args | arg ,
arg      => NUMBER|STRING
Type     => uint | int | byte | array | uint64 
stat     => if conds end | repetition do write end
conds    => condlist else write | condlist 
condlist => condlist elseif cond | cond
cond     => exp then block
repetition => for NAME = explist23 | for namelist in explist1
explist1   => explist1 , exp  | exp 
explist23  => exp , exp , exp | exp , exp 
exp        => exp or exp | exp and exp | exp opt exp | not exp |nil|true|false|arg
opt        => <= | < | >= | > | == | ~= | [-+*/]
""")


def parse_packet(pattern):
    return convert(parse('RE', pattern, PACKETGRAMMAR))


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



verify(PACKETGRAMMAR)