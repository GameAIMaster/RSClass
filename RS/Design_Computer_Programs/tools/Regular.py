def search(pattern, text):
    if pattern.startswith('^'):
        return match(pattern[1:], text)
    else:
        return match('.*' + pattern, text)
def match(pattern, text):
    """
    Return True if pattern appears at the start of text

    Please fill in the last line in this program.
    Namely: match(             ,           )

    We'll explain how we came to the code for the condition:
    elif len(pattern) > 1 and pattern[1] in '*?' in the next video lecture
    """

    if pattern == '':
        return True
    elif pattern == '$':
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and
                match(pattern[1:],text[1:]))  # fill in this line

def match1(p,text):
    if not text: return False
    else:
        return p == '.' or p == text[0]

def match_star(p, pattern, text):
    return (match(pattern, text) or match1(p, text) and match_star(p, pattern, text[1:]))

def test():
    assert search('^武燕*王东梁*!', '武燕王东梁梁梁梁梁!')
    assert search('baa*!', 'Sheep said baaaa humbug') == False
    assert match('baa*!', 'baaaaaaa! said the sheep')
    assert match('baa*!', 'Sheep said baaaa!') == False
    assert search('def', 'abcdefg')
    assert search('def$', 'abcdef')
    assert search('def$', 'abcdefg') == False
    assert search('^start', 'not the start') == False
    assert match('a*b*c*', 'just anything')
    assert match('x?', 'text')
    assert match('text?', 'tex')
    assert match('text?', 'tex')
    def words(text): return text.split()
    assert all(match('aa*bb*cc*$', s) for s in words('abc aaabbbcc aaaabcccc'))
    assert not any(match('aa*bb*cc*$', s)
        for s in words('ac aaabbbcccd aaaa-b-cccc'))
    assert all(search('^ab.*aca.*a$', s)
               for s in words('abracadabra abacaa about-acacia-fa'))
    assert all(search('t.p', s)
               for s in words('tip top tap atypical tepid stop'))
    assert not any(search('t.p', s)
                   for s in words('TYPE teepee tp'))
    return print('test passes')


# concepts: patterm, text->result,  partial result,control iteration,set or remind(消耗集合)
# 提供API创造自己的语言
#---------------
# User Instructions
#
# Fill out the API by completing the entries for alt,
# star, plus, and eol.


def lit(string):  return ('lit', string)
def seq(x, y):    return ('seq', x, y)
def alt(x, y):    return ('alt', x, y)
def star(x):      return ('star', x)
def plus(x):      return (seq(x,star(x)))
def opt(x):       return alt(lit(''), x) #opt(x) means that x is optional
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)

def test1():
    assert lit('abc')         == ('lit', 'abc')
    assert seq(('lit', 'a'),
               ('lit', 'b'))  == ('seq', ('lit', 'a'), ('lit', 'b'))
    assert alt(('lit', 'a'),
               ('lit', 'b'))  == ('alt', ('lit', 'a'), ('lit', 'b'))
    assert star(('lit', 'a')) == ('star', ('lit', 'a'))
    assert plus(('lit', 'c')) == ('seq', ('lit', 'c'),
                                  ('star', ('lit', 'c')))
    assert opt(('lit', 'x'))  == ('alt', ('lit', ''), ('lit', 'x'))
    assert oneof('abc')       == ('oneof', ('a', 'b', 'c'))
    return 'tests pass'

print (test1())


# ----------------
# User Instructions
#
# The function, matchset, takes a pattern and a text as input
# and returns a set of remainders. For example, if matchset
# were called with the pattern star(lit(a)) and the text
# 'aaab', matchset would return a set with elements
# {'aaab', 'aab', 'ab', 'b'}, since a* can consume one, two
# or all three of the a's in the text.
#
# Your job is to complete this function by filling in the
# 'dot' and 'oneof' operators to return the correct set of
# remainders.
#
# dot:   matches any character.
# oneof: matches any of the characters in the string it is
#        called with. oneof('abc') will match a or b or c.

def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        return set([text[len(x):]]) if any(text.startswith(c) for c in x) else null
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)


null = frozenset()


def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y


def test2():
    assert matchset(('lit', 'abc'), 'abcdef') == set(['def'])
    assert matchset(('seq', ('lit', 'hi '),
                     ('lit', 'there ')),
                    'hi there nice to meet you') == set(['nice to meet you'])
    assert matchset(('alt', ('lit', 'dog'),
                     ('lit', 'cat')), 'dog and cat') == set([' and cat'])
    assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
    assert matchset(('oneof', 'a'), 'aabc123') == set(['abc123'])
    assert matchset(('eol',), '') == set([''])
    assert matchset(('eol',), 'not end of line') == frozenset([])
    assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])

    return 'tests pass'


print(test2())


# ---------------
# User Instructions
#
# Complete the search and match functions. Match should
# match a pattern only at the start of the text. Search
# should match anywhere in the text.

def search(pattern, text):
    "Match pattern anywhere in text; return longest earliest match or None."
    for i in range(len(text)):
        m = match(pattern, text[i:])
        if m is not None : # your code here
            return m


def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = matchset(pattern, text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[0:len(text)-len(shortest)] # your code here

def test3():
    assert match(('star', ('lit', 'a')),'aaabcd') == 'aaa'
    assert match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == None
    assert match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'
    assert search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'
    return 'tests pass'

print(test3())