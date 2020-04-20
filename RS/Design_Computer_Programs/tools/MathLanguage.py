import string
"""
语法：Grammar
Exp     => Term[+-] Exp | Term
Term    => Factor [*/] Term | Factor
Factor  => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps    => Exp [,] Exps | Exp
Var     => [a-zA-Z_]\w*
Num     => [-+]?[0-9]+([.][0-9]*)?
缺少能理解这种语法的东西
"""
# 希望在计算机中存储方式
# G = {'Exp': (['Term', '[+-]', 'Exp'], ['Term'] ),
#      'Term': (['Factor', '[*/]', 'Term'] , ['Factor'])}

#删除开头结尾多余的空格
def split(text, sep=None, maxsplit=-1):
    "Like str.split applied to text, but strips whitespace from each piece"
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]

# 所以
def grammar(description, whitespace=r'\s*'):
    """Convert a desceiption to a grammar."""
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs!
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, '|')
        G[lhs] = tuple(map(split, alternatives))
    return G

G = grammar(r"""Exp => Term [+-] Exp | Term
Term    => Factor [*/] Term | Factor
Factor  => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps    => Exp [,] Exps | Exp
Var     => [a-zA-Z_]\w*
Num     => [-+]?[0-9]+([.][0-9]*)?""")

print(G)






