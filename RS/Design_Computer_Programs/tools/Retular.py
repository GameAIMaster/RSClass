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
    assert search('baa*!', 'Sheep said baaaa!')
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


test()