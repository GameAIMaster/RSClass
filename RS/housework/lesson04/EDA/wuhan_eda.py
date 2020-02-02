# 可视化EDA https://github.com/BlankerL/DXY-2019-nCoV-Data
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os
from matplotlib.font_manager import FontProperties

#config
pd.set_option('display.max_columns', 10)

# API 画折线图
def line_chart(provinceName):
    result = clean_df['provinceName']
    print()

# 测试用例
data = pd.read_csv('DXYArea.csv')
df = data[['provinceName', 'province_confirmedCount', 'updateTime']]
df['updateTime'] = df['updateTime'].str[0:10]
clean_df = df.drop_duplicates(['provinceName', 'updateTime'], keep='first')
print(clean_df)
# 折线图
line_chart("湖北省")
