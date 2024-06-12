from Design_Computer_Programs.tools.MathLanguage import *
# 利用trace调试到 /path? 不应该有空格写成/ path?  调试信息要成对出现，host应该能匹配完成却返回none，
# 说明问题在这解析出错
# --> parse_atom('/', '')
# <-- parse_atom('/', '') == (None, None) /没有被匹配
URL = grammar("""
url => httpaddress | ftpaddress | mailtoaddress
httpaddress => http:// hostport /path? ?search?
ftpaddress => ftp:// login / path ; ftptype | ftp:// login / path
/path? => / path | ()
?search? => [?] search | ()
mailtoaddress => mailto : xalphas @ hostname
hostport => host : port | host
host => hostname | hostnumber
hostname => ialpha . hostname | ialpha
hostnumber => digits . digits . digits . digits
ftptype => A formcode | E formcode | I | L digits
formcode => [NTC]
port => digits | path
path => void | segment / path | path
segment => xalphas
search => xalphas + search | search
login => userpassword hostport | hostport
userpassword => user : password @ | user @
user => alphanum2 user | alphanum2
password => alphanum2 password | password
path => void | segment / path | segment
void => ()
digits => digit digits | digit
digit => [0-9]
alpha => [a-zA-Z]
safe => [$-_@.&+-]
extra => [()!*''""]
escape => % hex hex
hex => [0-9a-fA-F]
alphanum => alpha | digit
alphanums => alphanum alphanums | alphanum
alphanum2 => alpha | digit | [-_.+]
ialpha => alpha xalphas | alpha
xalphas => xalpha xalphas | xalpha
xalpha => alpha | digit | safe | extra | escape
""")

url = 'http://www.google.com/'
print(parse('url', url, URL))
verify(URL)
