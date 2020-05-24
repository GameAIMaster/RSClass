from Design_Computer_Programs.tools.MathLanguage import *
URL = grammar("""
url => httpaddress | ftpaddress | mailtoaddress
httpaddress => http:// hostport / path? ?search?
ftpaddress => ftp:// login / path ; ftptype | ftp:// login / path
/path? => / path | ()
?search? => [?] search | ()
mailtoaddress => mailto : xalphas @ hostname
hostport => host : port | host
host => hostname | hostnumber
ftptype => A formcode | E formcode | I | L digits
formcode => [NTC]
port => digits | path
path => void | segment / path | path
segment => xpalphas
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
""", whitespace='()')


verify(URL)
