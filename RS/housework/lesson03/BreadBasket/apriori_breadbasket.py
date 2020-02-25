import pandas as pd
import time

#数据加载
data = pd.read_csv("BreadBasket_DMS.csv")
# print(data.head())
# Item转换成小写
data['Item'] = data['Item'].str.lower()
# 去掉none的商品
data = data.drop(data[data.Item == 'none'].index)

def rule1():
    from efficient_apriori import apriori
    start = time.time()
    # 将transaction作为键，Item作为值创建数据结构
    map = data.set_index('Transaction')['Item']

    temp_t = 0
    transactions = []
    # 区分keys,values,items
    for i, v in map.items():
        if i != temp_t:
            temp_t = i
            temp_set = set()
            temp_set.add(v)
            transactions.append(temp_set)
        else:
            temp_set.add(v)
    # 挖掘频繁项集和关联规则
    itemset, rules = apriori(transactions, min_support=0.02, min_confidence=0.5)
    print('频繁项集：', itemset)
    print('关联规则：', rules)
    end = time.time()
    print('计算用时：%s' % (end-start))
# rule1()

def encode_units(x):
    if x <=0:
        return 0
    if x >=1:
        return 1

# 采用mxlend.frequent_patterns工具包
def rule2():
    from mlxtend.frequent_patterns import apriori, association_rules
    pd.options.display.max_columns = 100
    start = time.time()
    #将数据行列互换展开去重
    hot_encoded_df = data.groupby(['Transaction', 'Item'])['Item'].count().unstack().reset_index().fillna(0).set_index('Transaction')
    hot_encoded_df = hot_encoded_df.applymap(encode_units)
    frequent_items = apriori(hot_encoded_df, min_support=0.02, use_colnames=True)
    rules = association_rules(frequent_items, metric='lift', min_threshold=0.5)
    print('频繁项集：', frequent_items)
    print('关联规则：', rules)
    end = time.time()
    print('计算用时：%s' % (end - start))
rule2()
