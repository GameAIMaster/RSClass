from Design_Computer_Programs.tools.MathLanguage import *
PACKETGRAMMAR = grammar("""
packet     => _G. packetType packetName [=] BasePacket:New[(]PacketID. pakidname [)] semi?
semi?      => [.;] | ()
packetType => CG | GC
packetName => name
pakidname  => name
fullvar    => prefixexp var
write      => index = self:Write writeType args semi?
args      =>  [(] explist1 [)] | [(] [)] | string
var       => name [[] exp []] | name
prefixexp  => name [.] prefixexp | ()
writeType  => name

writelist  => write writelist | write
repetition => for fullvar = explist23 
explist1   => exp , explist1 | exp 
explist23  => exp , exp , exp | exp , exp 
stat       => if conds end | repetition do writelist end
exp        => nil | true | false | string | number  |not exp | fullvar or exp | fullvar and exp | fullvar opt exp | fullvar 
opt        => <= | < | >= | > | == | ~= | [-+*/%]

conds      => condlist else writelist
condlist   => cond elseif condlist | cond
cond       => [(] exp [)] then writelist | exp then writelist  
laststat   => break
laststat   => return
laststat   => return explist1

useless    => [?!_G] | [?!Write] | [?!if] | [?!for]

string     => "[^"]*"
name       => [a-zA-Z_][a-zA-Z0-9_]*
number     => int frac | int
int => -?\d[0-9]*
frac => [.][0-9]+
""")
'''
write    => Write Type [(] args stream, index, size [)] semi?
这句感觉设计的不好
var       => prefixexps . name [[] exp []] | prefixexps . name | name [[] exp []] | name |  number 
https://blog.csdn.net/abcjennifer/article/details/46821401
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
        index = self:WriteINT32(self.m_ItemIndex[i], stream, index, size);
    end"""
iftest = """if self.m_count == 1 then
        index = self:WriteByte(self.m_ItemIndex[i], stream, index, size);
        index = self:WriteINT32(self.m_ItemIndex[i], stream, index, size);
        elseif (self.md[3]) then
        index = self:WriteByte(self.m_ItemIndex[i], stream, index, size);
        index = self:WriteINT32(self.m_ItemIndex[i], stream, index, size);
        else
        index = self:WriteByte(self.m_ItemIndex[i], stream, index, size);
        index = self:WriteINT32(self.m_ItemIndex[i], stream, index, size);
    end"""

useless = """
    _G.GCPickUpPackage = BasePacket:New(PacketID.PACKET_GC_PACKUP_PACKET);

GCPickUpPackage.m_nResult = 0; -- int

function GCPickUpPackage:GetSize()
    return 1 + 1 + 1 + 1;
end

function GCPickUpPackage:ReadStream(stream, index, size)
    ------------------------以下协议解析过程
    print("----------------GCPickUpPackage:ReadStream-------------------------size = " .. size);

    index, self.m_nResult = self:ReadInt32(stream, index, size);

    return index;

end

--[Comment]
--处理完毕
function GCPickUpPackage:Execute()
    --第二个参数没有意义
    LuaBagManager.bIsArranging = false;
    --if (ChangeEquipManager.Instance != null)
    --    ChangeEquipManager.Instance.onPickUpCompleted ();
    --Debug.Log(Time.realtimeSinceStartup);
    --CEventSender.SendEvent(LuaEvent.ShowPublicTip, Util.LangUtil.GetKey(60273));
    EventSender.SendEvent(LuaEvent.TidyBag,1);
end

function GCPickUpPackage:Clear()
    GCPickUpPackage.m_nResult = 0; -- int
end
"""
# print(parse('packet', packet, PACKETGRAMMAR))
# print(parse('write', write, PACKETGRAMMAR))
# print(parse('stat', fortest, PACKETGRAMMAR))
# print(parse('stat', iftest, PACKETGRAMMAR))