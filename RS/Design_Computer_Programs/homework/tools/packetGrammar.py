from Design_Computer_Programs.tools.MathLanguage import *
from Design_Computer_Programs.homework.tools.unparse import Unparser
PACKETGRAMMAR = grammar("""
packet     => _G. packetType packetName [=] BasePacket:New[(]PacketID. pakidname [)] semi?
semi?      => [.;] | ()
packetType => CG | GC
packetName => name
pakidname  => name
fullvar    => prefixexp var
write      => index = self:Write writeType args semi?
read       => index, fullvar = self:Read readType args semi?
args      =>  [(] explist1 [)] | [(] [)] | string
var       => name [[] exp []] | name
prefixexp  => name [.] prefixexp | ()
writeType  => name
readType   => name

writeorreadlist  => write writeorreadlist | read writeorreadlist | write | read
repetition => for var = explist23 
explist1   => exp , explist1 | exp 
explist23  => exp , exp , exp | exp , exp 

statlist   => stat statlist | stat

conds      => cond eliflist else statlist | cond eliflist | cond
cond       => [(] exp [)] then statlist | exp then statlist
stat       => if conds end | repetition do statlist end | writeorreadlist

exp        => preexplist remindexp | remindexp
remindexp  => arg
arg        => nil | true | false | string | number | fullvar 
preexplist => preexp preexplist | preexp
preexp     => arg opt 
opt        =>  and | or | <= | < | >= | > | == | ~= | [-+*/%] 


eliflist   => elseif cond eliflist | () 

laststat   => break
laststat   => return
laststat   => return explist1

uselesslist => useless uselesslist | useless
useless    => ((?!index\\s?[=])(?!index,\\s?(?!size))(?!_G)(?!if)(?!for).)+

file       => ?uselesslist packet uselesslist writeorreadlist ?uselesslist ?statlist ?writeorreadlist ?uselesslist
?uselesslist => uselesslist | ()
?repetition  => repetition | ()
?statlist    => statlist | ()
?writeorreadlist   => writeorreadlist | ()

string     => "[^"]*"
name       => [a-zA-Z_][a-zA-Z0-9_]*
number     => int frac | int
int => -?\d[0-9]*
frac => [.][0-9]+
""")

fail = (None, None)

packet = "_G.CGUseItem = BasePacket:New(PacketID.PACKET_CG_USEITEM);"
write = "index = self:WriteUInt64(l, h, stream, index, size)"
fortest = """for i = 0, self.m_count-1 do
        index = self:WriteByte(self.m_ItemIndex[i], stream, index, size);
        index = self:WriteINT32(self.m_ItemIndex[i], stream, index, size);
    end"""
iftest = """if CGAskCaptainBookOpt.nOptType >= 5 and CGAskCaptainBookOpt.nOptType <= 4 then
                index = self:WriteInt32(CGAskCaptainBookOpt.nBookEventID, stream, index, size)
            elseif CGAskCaptainBookOpt.nOptType == 3 then
                index = self:WriteInt32(CGAskCaptainBookOpt.nBookEventID, stream, index, size)
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

useless_test = """
--获得活动增强标识 
_G.GCActivityRewardUpgrade = BasePacket:New(PacketID.PACKET_GC_ACTIVITY_REWARD_UPGRADE);

GCActivityRewardUpgrade.m_FlagType = 0;
GCActivityRewardUpgrade.m_FlagIcon = 0;

function GCActivityRewardUpgrade:GetSize()
    return 1;
end

function GCActivityRewardUpgrade:ReadStream(stream, index,size)
    index,self.m_Type = self:ReadByte(stream,index,size)
    index, GCActivityRewardUpgrade.m_FlagType = self:ReadInt32(stream, index, size); 
    index, GCActivityRewardUpgrade.m_FlagIcon0  = self:ReadInt32(stream, index, size); 
    
    if GCActivityRewardUpgrade.m_FlagIcon == 2 then
        for i = 0, self.m_count-1 do
            if GCActivityRewardUpgrade.m_FlagIcon == 2 then
                index, GCActivityRewardUpgrade.m_FlagIcon10  = self:ReadInt32(stream, index, size); 
            end
            index, GCActivityRewardUpgrade.m_FlagIcon1  = self:ReadInt32(stream, index, size); 
            index, GCActivityRewardUpgrade.m_FlagIcon2  = self:ReadInt32(stream, index, size);
        end
        index, GCActivityRewardUpgrade.m_FlagIcon3  = self:ReadInt32(stream, index, size); 
        index, GCActivityRewardUpgrade.m_FlagIcon4  = self:ReadInt32(stream, index, size);
    end
    
    for i = 0, self.m_count-1 do
        index, GCActivityRewardUpgrade.m_FlagIcon5  = self:ReadInt32(stream, index, size); 
        index, GCActivityRewardUpgrade.m_FlagIcon6  = self:ReadInt32(stream, index, size);
    end
    
    --printe("GCActivityRewardUpgrade:ReadStream",GCActivityRewardUpgrade.m_FlagType,GCActivityRewardUpgrade.m_FlagIcon);
    return index;
end

function GCActivityRewardUpgrade:Execute()
    ActivityModule:SetRewardFlag(ActivityModule.RewardFlag.Upgrade,GCActivityRewardUpgrade.m_FlagType,GCActivityRewardUpgrade.m_FlagIcon);
end

function GCActivityRewardUpgrade:Clear()
    GCActivityRewardUpgrade.m_FlagType = 0;
    GCActivityRewardUpgrade.m_FlagIcon = 0;
end
"""
# print(parse('packet', packet, PACKETGRAMMAR))
# print(parse('write', write, PACKETGRAMMAR))
# print(parse('stat', fortest, PACKETGRAMMAR))
# print(parse('stat', iftest, PACKETGRAMMAR))

tree = parse('file', useless_test, PACKETGRAMMAR)
print(tree)

Unparser(tree[0]) # , 'E:\\tick\\RS\\Design_Computer_Programs\\homework\\tools'