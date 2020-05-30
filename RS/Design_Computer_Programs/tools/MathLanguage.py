import re
import pickle # 泡菜，用来保存编译后的结果到硬盘上
from Design_Computer_Programs.tools.Memoization import *
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


# >>> parse('Exp', 'a * x', G)
# (['Exp', ['Term',['Factor', ['Var', 'a']],
#  '*',
#  ['Term',['Factor', ['Var', 'x']]]]],'')

@trace
def parse(start_symbol, text, grammar):
    """Example call: parse('Exp', '3*x + b, G.
    Returns a (tree, remainder) pair. if reminder is ''. it parsed the whole
    string. Failure iff remainder is None.This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first(将长的解析放到左侧);don't do 'E=> T | T op E'
    Also, no left recursion allowed:don't do 'E=> T | T op E'"""

    tokenizer = grammar[' '] + '(%s)'

    @trace
    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    @trace
    @memo #提高性能，防止匹配不成功重新匹配
    def parse_atom(atom, text):
        if atom in grammar: # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem
            return Fail
        else: # Terminal: match characters against start of text 从text中除去带有空格的atom
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])

    # Body of parse:
    return parse_atom(start_symbol, text)
Fail = (None, None)

# print(parse('Exp', 'wq * x + 3', G))

# print(re.match("\\s*(%s)" % '-?\d[0-9]*', ''' 0, self.m_count-1 do
#         index = self:WriteByte(self.m_ItemIndex[i], stream, index, size);
#     end'''))




