from Design_Computer_Programs.tools.MathLanguage import *

JSON = grammar("""
json => value 
obj  => [{] pairs [}] | [{] [}]
pairs => pair [,] pairs | pair
pair => STRING [:] value
arr  => [[] values []] | [[] []]
value => STRING | NUMBER | obj | arr  | [true]  | [false]  | [null]
values => value [,] values | value
STRING => ["] SAFECODEPOINT ["]
ESC => [\] ["\/bfnrt] | [\] UNICODE
UNICODE => [u] HEX HEX HEX HEX
HEX => [0-9a-fA-F]
SAFECODEPOINT => [\u4e00-\u9fa5_0-9a-zA-Z]+
NUMBER => [-]? INT ([.][0-9]+)?
INT => [0] | [1-9] [0-9]*
""")
json = '{"age": 21}'
print(parse('json', json, JSON))