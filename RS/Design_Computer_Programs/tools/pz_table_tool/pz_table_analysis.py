"""概念清单：
        表：路径，表名.后缀名
        资源：路径，资源名.后缀名
        内容：ID，属性类型，属性名，注释，数据
        连接：名称，ID
        流程：set((动作，表/资源),(动作，表/资源),(动作，表/资源)...)
        """
files_id = {}

# 遍历文件夹将文件存放到list中


id_list = []
def find_related_res(filename):
    """根据输入的文件名找到相关资源或表格,返回相关文件，('add',path)/('modify',file)"""
    id = find_id_by_filename(filename) # 获取文件唯一id
    wuf = loadwuf()
    if id is not None:
        unicom_id = find_unicom_id(id)# 返回联通分量标识符
        if unicom_id is not None:
            unicom = wuf.find(unicom_id)#返回分量集合
            return unicom

def loadwuf():
    N = len(files_id)# 所有文件数量
    wuf = WeightedQuickUF(N)

def find_id_by_filename(filename):
    """数据结构为file:id"""
    return files_id[filename]

def find_unicom_id(id):
    return id_list[id]

class WeightedQuickUF():
    def __init__(self, N):
        self.N = N
        self.count = N
        self.id_list = [i for i in range(N) ]
        self.sz_list = [1 for i in range(N)]
    def get_count(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while (p != self.id_list[p]):
            p = self.id_list[p]
        return p
    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if(i == j ):
            return
        if(self.sz_list[i] < self.sz_list[j]):
            self.count = self.count - 1


# -*- coding: utf-8 -*-
import os.path

# TODO：这里填自己的文件路径
m_Path_List = ["D:\PZ_res\Res\ConfigTables\Public\Scene"]

def walkFile():
    count = 0
    for pathlist in m_Path_List:
        for path, dir_list, file_list in os.walk(m_Path_List):
            for i , file_name in enumerate(file_list):
                files_id[file_name] = i + count
            count += len(file_list)

    #  持久化

def analysis_file_list():
    # 对所有的表进行
    print()
