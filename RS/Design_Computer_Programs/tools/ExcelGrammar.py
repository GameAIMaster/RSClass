from Design_Computer_Programs.tools.MathLanguage import *
# 利用trace调试到 /path? 不应该有空格写成/ path?  调试信息要成对出现，host应该能匹配完成却返回none，
# 说明问题在这解析出错
# --> parse_atom('/', '')
# <-- parse_atom('/', '') == (None, None) /没有被匹配
Excle = grammar("""
Exp => Term [+-] Exp | Term
Term => Factor [*/] Term | Factor
Factor => Stat | [+-] [(] Exp [)] | [(] Exp [)] | Funcall | Var | Num 
Funcall => Find | IsNumber | Var [(] ExpList [)] | Var [(] CondList [)] |  Var [(] [)]
ExpList => Exp [,] ExpList | Exp
Stat => IF [(] Conds [,] Exp [,] Exp [)]
LogicStr => IF [(] Conds [,] Str [,] Str [)]
TextList => LogicStr [&]+ TextList | LogicStr | [\"'] Text [\"'] [&]+ TextList | Text [&]+ TextList | [\"'] Text [\"'] | Num | [\"'] [\"'] [&]+ TextList | [\"'] [\"']
Str => TextList
Conds =>  Cond | [(] Cond [)] 
Find => FIND [(] [\"'] Text [\"'] [,] [\"'] Text [\"'] , Num [)] | FIND [(] [\"'] Text [\"'] [,] [\"'] Text [\"'] [)]
IsNumber => ISNUMBER [(] [\|']? Text [\|']? [)] | ISNUMBER [(] Num [)]
CondList => [(] Cond [)] [,] CondList |  Cond [,] CondList | Cond
Cond => [\"'] Text [\"'] = [\"'] Text [\"'] | Exp >= Exp | Exp <= Exp | Exp > Exp | Exp < Exp | Exp = Exp 
Var => [a-zA-Z_]+
Text => [^\"^'^&]*
Num => [-+]?[0-9]+([.][0-9]*)? 
""")
# verify(Excle)
print(parse('Str', 'IF(0=1,\"±2\",100)', Excle))
#正则表达式 不包含" ' & 三个字符