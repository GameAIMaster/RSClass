# -*- coding: UTF-8 -*-
# ---------------
# User Instructions
#
# Write a function, findtags(text), that takes a string of text
# as input and returns a list of all the html start tags in the
# text. It may be helpful to use regular expressions to solve
# this problem.

import re

def findparams(text):
    parms = '(\s*[\w+.]*\w+\s*,)+'
    tags = '(Write\w+[(]\s*' + parms + '\s*stream)'
    # findtag = '(<\s*\w+\s*(\w+\s*=\s*"[^"]*"\s*)*\s*/?>)'
    return [a for a,b in re.findall(tags, text)]
    # return re.findall(findtag, text)
    # return re.findall('(\w+)*', 'abc')

testtext1 = """
function CGUseItem:WriteStream(stream, index, size)

    index = self:WriteByte(self.m_BagIndex, stream, index, size);
    index = self:WriteInt32(self.m_BagTableIndex, stream, index, size);
    local l, h = 0, 0
    if self.m_BagGUID ~= nil then
        l, h = uint64.tonum2(self.m_BagGUID)
    end
    index = self:WriteUInt64(l, h, stream, index, size);
    index = self:WriteByte(self.m_UseNum, stream, index, size);
    index = self:WriteInt32(self.m_TargetObj, stream, index, size);
    index = self:WriteSingle(self.m_TargetPos.x, stream, index, size);
    index = self:WriteSingle(self.m_TargetPos.y, stream, index, size);
    index = self:WriteSingle(self.m_Dir, stream, index, size);
    if self.m_TargetPetGUID ~= nil then
        l, h = uint64.tonum2(self.m_TargetPetGUID) 
    end
    index = self:WriteUInt64(l, h, stream, index, size);
    index = self:WriteByte(self.m_TargetItemIndex, stream, index, size);
    index = self:WriteByte(self.m_UseFrom, stream, index, size);
    if self.m_bSelect == nil then
        self.m_bSelect = 0
    end
    index = self:WriteByte(self.m_bSelect, stream, index, size);
    if self.m_bSelect == 1 then
        for i = 1, self.MaxSelectLen do
            if self.m_SelectArray[i] ~= nil then
                index = self:WriteInt32(self.m_SelectArray[i], stream, index, size);
            else
                index = self:WriteInt32(0, stream, index, size);
            end

        end
    end
    return index;
end
"""

def test():
    print(findparams(testtext1))
    assert findparams(testtext1) == ['<a href="www.udacity.com">',
                                   '<b>',
                                   '<a href="www.udacity.com"target="_blank">']
    return 'tests pass'

print(findparams(testtext1))