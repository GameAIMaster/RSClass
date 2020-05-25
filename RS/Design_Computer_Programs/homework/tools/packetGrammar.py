from Design_Computer_Programs.tools.MathLanguage import *
PACKETGRAMMAR = grammar("""
packet     => _G. packetType packetName [=] BasePacket:New[(]PacketID. pakidname [)] semi?
semi?      => [.;] | ()
packetType => CG | GC
packetName => name
pakidname  => name

write      => index = self:Write writeType [(] args [)] semi?
args      => arg , args | arg 
arg       => prefixexps . name | prefixexp [[] exp []] | name |  number
prefixexps  => prefixexp prefixexps | prefixexp
prefixexp  => name
writeType  => name

writelist  => write writelist | write
repetition => for arg = explist23 | for namelist in explist1
explist1   => exp explist1 | exp 
explist23  => exp , exp , exp | exp , exp 
stat       => repetition do writelist end
exp        => nil | true | false | string | number |  not exp | exp or exp | exp and exp | exp opt exp |  arg 
opt        => <= | < | >= | > | == | ~= | [-+*/%]

string     => "[^"]*"
name       => [a-zA-Z_][a-zA-Z0-9_]*
number     => int frac | int
int => -?\d[0-9]*
frac => [.][0-9]+
""")
'''
write    => Write Type [(] args stream, index, size [)] semi?


Type     => uint | int | byte | array | uint64 
stat     => if conds end | repetition do write end
conds    => condlist else write | condlist 
condlist => condlist elseif cond | cond
cond     => exp then block
repetition => for string = explist23 | for namelist in explist1


'''

def parse_packet(pattern):
    return convert(parse('RE', pattern, PACKETGRAMMAR))


def convert(tree):
    "Convert a REGRAMMAR parse tree into our regex (compiler) API"
    root = tree[0]
    names = {
        'optplus': 'plus(opt({x}))',
        'plusopt': 'opt(plus({x}))',
        'staropt': 'opt(star({x}))',
        'optstar': 'star(opt({x}))',
    }
    if isinstance(tree, list):
        try:
            if root in ('plus', 'star', 'opt', 'lit'):
                return '{r}({x})'.format(r=root, x=convert(tree[1]))
            elif root in ('optplus', 'plusopt', 'staropt', 'optstar'):
                return names[root].format(x=convert(tree[1]))
            elif root == 'oneof':
                return 'oneof({x})'.format(x=convert(tree[2]))
            elif root == 'group':
                return convert(tree[2])
            elif root == 'alt':
                if len(tree) == 2:
                    return convert(tree[1])
                else:
                    return 'alt({a}, {b})'.format(a=convert(tree[1]),
                                                  b=convert(tree[3]))
            elif root in ('seq', 'lits'):
                if len(tree) == 2:
                    return convert(tree[1])
                else:
                    return 'seq({a})'.format(a=', '.join(map(convert, tree[1:])))
            else:
                return convert(tree[1])
        except Exception as err:
            print('tree: {t}'.format(t=tree))
            raise
    else:
        return repr(tree)


fail = (None, None)

packet = "_G.CGUseItem = BasePacket:New(PacketID.PACKET_CG_USEITEM);"
write = "index = self:WriteUInt64(l, h, stream, index, size)"
fortest = """for i = 0, self.m_count-1 do
        index = self:WriteByte(self.m_ItemIndex[i], stream, index, size);
    end"""
# print(parse('packet', packet, PACKETGRAMMAR))
# print(parse('write', write, PACKETGRAMMAR))
print(parse('stat', fortest, PACKETGRAMMAR))