# RSClass - 推荐系统学习项目

这是一个综合性的推荐系统（Recommendation System）学习项目，涵盖了计算机程序设计、机器学习、数据挖掘等多个领域的实践案例和算法实现。

## 📁 项目结构

```
RSClass/
├── RS/
│   ├── Design_Computer_Programs/    # 计算机程序设计
│   │   ├── export_problem/          # 经典算法问题
│   │   ├── homework/                # 课程作业
│   │   ├── poker/                   # 扑克游戏算法
│   │   ├── probility_problem/       # 概率问题
│   │   ├── tools/                   # 工具模块
│   │   └── zebra_puzzle/            # 斑马谜题
│   └── housework/                   # 机器学习实战
│       ├── lesson01/                # 第一课：机器学习基础
│       ├── lesson02/                # 第二课：数据挖掘
│       ├── lesson03/                # 第三课：关联规则挖掘
│       └── lesson04/                # 第四课：网络分析
├── mnist_keras.py                   # MNIST 数据集 Keras 实现
└── mnist_lr.py                      # MNIST 数据集逻辑回归实现
```

## 🎯 主要内容

### 1. 计算机程序设计 (Design_Computer_Programs)

#### 🧩 经典算法问题 (export_problem)
- **桥梁问题** (`bridge_problem.py`) - 解决过桥最优时间问题
- **过河问题** (`cross_river.py`) - 渡河策略优化
- **传教士和野人问题** (`missionaries_cannibals.py`) - 经典AI搜索问题
- **倒水问题** (`pour_problem.py`) - 水壶容量问题求解

#### 🔧 工具模块 (tools)
- **JSON解析器** (`JSON_parser.py`) - JSON语法分析器实现
- **正则表达式语法** (`REGrammar.py`) - 正则表达式语法解析
- **数学语言处理** (`MathLanguage.py`) - 数学表达式处理
- **记忆化装饰器** (`Memoization.py`) - 性能优化工具

#### 🎮 概率问题 (probility_problem)
- **条件概率** (`condictional_probility.py`) - 条件概率计算
- **游戏理论** (`game_theory.py`) - 博弈论算法
- **掷骰子游戏** (`play_pig.py`, `play_pig_d.py`, `play_pig_optimal.py`) - 策略优化

### 2. 机器学习实战 (housework)

#### 📊 第一课：机器学习基础
- **线性回归** (`linear_regression.py`) - 房价预测等回归问题
- **逻辑回归** (`logic_regression.py`) - 分类问题解决
- **MNIST手写数字识别** (`mnist_cart.py`) - 决策树分类
- **航班延误预测** (`departure_prediction/`) - 时间序列预测

#### 🔍 第二课：数据挖掘
- **泰坦尼克号数据分析** (`titanic/`) - 生存预测分析
- **蒸汽游戏数据** (`steam_video_games/`) - 游戏数据清洗分析
- **美食标签聚类** (`delicious-2k/`) - 文本聚类分析
- **团队聚类分析** (`team_cluster/`) - K-means聚类实践

#### 🛒 第三课：关联规则挖掘
- **购物篮分析** (`BreadBasket/`) - Apriori算法实现
- **电影演员关联** (`MovieActors/`) - 关联规则挖掘
- **电影推荐** (`MovieLens/`) - 协同过滤算法
- **市场篮子优化** (`homework/MarketBasket.py`) - 购买行为分析

#### 🌐 第四课：网络分析
- **PageRank算法** (`pagerank/`) - 网页重要性排序
- **TextRank算法** (`textrank/`) - 文本摘要提取
- **最短路径** (`shortest_path/`) - Floyd算法实现
- **疫情数据分析** (`EDA/`) - COVID-19数据探索

## 🚀 快速开始

### 环境要求

```bash
Python >= 3.7
pip install -r requirements.txt
```

主要依赖：
- `numpy` - 数值计算
- `pandas` - 数据处理
- `scikit-learn` - 机器学习
- `matplotlib` - 数据可视化
- `tensorflow/keras` - 深度学习
- `networkx` - 网络分析

### 运行示例

#### 1. 运行经典算法问题
```bash
cd RS/Design_Computer_Programs/export_problem/
python bridge_problem.py
```

#### 2. 机器学习案例
```bash
cd RS/housework/lesson01/
python linear_regression.py
```

#### 3. MNIST手写数字识别
```bash
python mnist_keras.py
# 或
python mnist_lr.py
```

## 📚 学习路径

### 初学者
1. 从 `Design_Computer_Programs/export_problem/` 开始学习基础算法
2. 学习 `housework/lesson01/` 中的机器学习基础
3. 实践 `titanic/` 数据分析案例

### 进阶学习
1. 深入学习 `lesson03/` 中的关联规则挖掘
2. 探索 `lesson04/` 中的网络分析算法
3. 研究推荐系统的具体实现

### 高级应用
1. 结合多个模块实现完整的推荐系统
2. 优化算法性能和准确率
3. 扩展到实际业务场景

## 🔍 关键特性

- **完整的学习体系** - 从基础算法到高级应用
- **实战导向** - 真实数据集和业务场景
- **代码质量高** - 详细注释和测试用例
- **算法丰富** - 涵盖机器学习、数据挖掘、网络分析等
- **可扩展性强** - 模块化设计，易于扩展

## 📖 主要算法

### 机器学习算法
- 线性回归 (Linear Regression)
- 逻辑回归 (Logistic Regression)  
- 决策树 (Decision Tree)
- K-means聚类

### 推荐系统算法
- 协同过滤 (Collaborative Filtering)
- 内容相似度计算
- 关联规则挖掘 (Apriori)

### 网络分析算法
- PageRank算法
- TextRank算法
- 最短路径算法 (Floyd)

### 搜索算法
- 广度优先搜索 (BFS)
- 深度优先搜索 (DFS)
- 状态空间搜索

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目仅用于学习目的。

## 📞 联系方式

如有问题或建议，请通过 GitHub Issues 联系。

---

*这是一个用于学习推荐系统和机器学习算法的综合性项目，适合计算机科学专业学生和对推荐系统感兴趣的开发者。*