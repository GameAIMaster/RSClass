# 数据格式为Dec 2 2020  wangzhihua017   feature/PanoReplace
# Oct 10 2020 wanglei334      feature/ConvertToImage
# Mar 29 2020 liuhui123       nanyu_1_0
# 我想替换日期为2020-12-02  wangzhihua017   feature/PanoReplace
# txt文件
import re
import os
import time
result = []
def replace_date(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = re.sub(r'(\w{3}) (\d{1,2}) (\d{4})', r'\3-\1-\2', line)
            # 替换Oct 为 10
            line = re.sub(r'Jan', '01', line)
            line = re.sub(r'Feb', '02', line)
            line = re.sub(r'Mar', '03', line)
            line = re.sub(r'Apr', '04', line)
            line = re.sub(r'May', '05', line)
            line = re.sub(r'Jun', '06', line)
            line = re.sub(r'Jul', '07', line)
            line = re.sub(r'Aug', '08', line)
            line = re.sub(r'Sep', '09', line)
            line = re.sub(r'Oct', '10', line)
            line = re.sub(r'Nov', '11', line)
            line = re.sub(r'Dec', '12', line)
            print(line)
            result.append(line)

replace_date('C:\\Users\\User\\Documents\\git.txt')
# 将result写入文件result.txt
with open('C:\\Users\\User\\Documents\\result.txt', 'w', encoding='utf-8') as f:
   for line in result:
        f.write(line)
