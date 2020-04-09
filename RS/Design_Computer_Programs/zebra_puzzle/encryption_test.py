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