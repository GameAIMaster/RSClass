# 试用networkX计算节点的pagerank
import networkx as nx
import matplotlib.pyplot as plt

# 创建有向图[("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
# edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
edges = [("D", "A"), ("B", "C"), ("C", "D"), ("D", "B")]
# 在有向图中添加边的集合
G = nx.DiGraph()
for edge in edges:
    G.add_edge(edge[0], edge[1])
# 有向图可视化
layout = nx.spring_layout(G)
nx.draw(G, pos=layout, with_labels=True, hold=False)
plt.show()

# 计算简化模型的PR值
pr = nx.pagerank(G, alpha=1)
pagerank_list = {node: rank for node, rank in pr.items()}
print("简化模型的PR值：", pr)
# 计算随机模型的PR值
pr = nx.pagerank(G, alpha=0.85)
print("随机模型的PR值：", pr)