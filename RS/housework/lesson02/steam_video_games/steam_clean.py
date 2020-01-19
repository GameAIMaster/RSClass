import numpy as np
import pandas as pd
import random

path = 'steam-200k.csv'
df = pd.read_csv(path, header=None, names=['UserID', 'Game', 'Action', 'Hours', 'Not Needed'])
# 数据探索 观察数据发现，购买时时长为1，玩游戏会产生新的一条数据
print('显示前5条数据')
print(df.head())
print('显示数据大小')
print(df.shape)

# 创建Hours_Player字段，替代原有的Action和Hours，0表示仅购买，大于0表示购买的游戏时长
df['Hours_Player'] = df['Hours'].astype('float32')
df.loc[(df['Action'] == 'purchase') & (df['Hours'] == 1.0), 'Hours_Player'] = 0
print(df.head())
print('增加了Hours_Player 字段后，数据大小')
print(df.shape)
# 对数据从小到大排序， df下标也会发生变化
df.UserID = df.UserID.astype('int')
df.sort_values(['UserID', 'Game', 'Hours_Player'], ascending=True)
# 删除重复项，并保留最后一项出现的项（因为最有意向是用户游戏时间，第一项为购买）
clean_df = df.drop_duplicates(['UserID', 'Game'], keep='last')
# 去掉不用的列：Action，Hours, Not Needed
clean_df.drop(['Action', 'Hours', 'Not Needed'], axis=1)

print('删除重复项后的数据集：')
print(clean_df.head())
print(clean_df.shape)

# 探索数据集的特征
n_user = len(clean_df['UserID'].unique())
n_game = len(clean_df['Game'].unique())
print('数据集中包含了{0}玩家，{1}游戏'.format(n_user, n_game))
# 矩阵的稀疏性
sparsity = clean_df.shape[0] / float(n_user * n_game)
print('用户行为矩阵的稀疏性(填充比例)为{:.2%}'.format(sparsity))

