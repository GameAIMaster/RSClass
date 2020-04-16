import string,re
import itertools
table = str.maketrans('ABC','123')
f = 'A+B == C'
print(eval(f.translate(table)))

def solve(formula):
    # input "ODD + ODD == EVEN"填充数字 output: 数字替换字符或返回None
    for v in fill_in(formula):
        if valid(v):
            return v

def fill_in(formula):
    # 返回所有能够替换字符的数字
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(re.findall('[A-Z]', formula)) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def valid(f):
    try:
        return not re.search('\b0[0-9]', f) and eval(f) is True # 正则式排除了0开头的数字
    except ArithmeticError:
        return False

# for digits in itertools.permutations('1234567890', 3):
#     print(''.join(digits))

# print(re.findall('[A-Z]', '0Z34'))

# 通过trace发现eval执行了太多的时间，执行太多不必要的工作
# 通过将计算制作成lamuda表达式

# f = lambda A,B,C:A+B+C
# print(f(1,2,3))

def compile_word(word):
    # E.g compile word 'YOU' return '(1*U + 10*O + 100*Y)
    # if '+' return '+'
    if word.isupper():
        # result = '+'.join(['1'+'0'*i+'*'+v for i, v in enumerate(word[::-1])])
        result = '+'.join(['%s*%s' % (10**i, v) for i, v in enumerate(word[::-1])])
        print (result)
        return '('+ result + ')'
    else:
        return word

# print(compile_word("YOU"))

# 改进
def fast_solve(formula):
    f,letters = compile_formula(formula)
    for digits in itertools.permutations([1,2,3,4,5,6,7,8,9,0], len(letters)):
        if f(*digits) is True:
            table = str.maketrans(letters, ''.join(map(str, digits))) # 数字映射成字符串
            return formula.translate(table)
        else:
            pass


def compile_formula(formula, verbose=False):

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    first_letters = set(re.findall(r'\b([A-Z])[A-Z]',formula))
    params = ','.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula)) #正则加（）是保留分割项
    if first_letters:
        tests = ' and '.join([L+" != 0" for L in first_letters])
        body = '%s and (%s)' % (''.join(tokens),tests )
    lm = 'lambda ' + params +':' + body
    print(lm)
    return eval(lm), letters

print(fast_solve("ODD+ODD==EVEN"))
print(re.findall(r'\b([A-Z])[A-Z]',"AB + B == BA"))
# print(re.split('([A-Z]+)', "ODD+ODD==EVEN",))
