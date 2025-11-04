# RSClass - Recommendation System Learning Project

This is a comprehensive Recommendation System learning project that covers practical cases and algorithm implementations across multiple domains including computer programming, machine learning, and data mining.

## 📁 Project Structure

```
RSClass/
├── RS/
│   ├── Design_Computer_Programs/    # Computer Program Design
│   │   ├── export_problem/          # Classic Algorithm Problems
│   │   ├── homework/                # Course Assignments
│   │   ├── poker/                   # Poker Game Algorithms
│   │   ├── probility_problem/       # Probability Problems
│   │   ├── tools/                   # Tool Modules
│   │   └── zebra_puzzle/            # Zebra Puzzle
│   └── housework/                   # Machine Learning Practice
│       ├── lesson01/                # Lesson 1: Machine Learning Basics
│       ├── lesson02/                # Lesson 2: Data Mining
│       ├── lesson03/                # Lesson 3: Association Rule Mining
│       └── lesson04/                # Lesson 4: Network Analysis
├── mnist_keras.py                   # MNIST Dataset Keras Implementation
└── mnist_lr.py                      # MNIST Dataset Logistic Regression Implementation
```

## 🎯 Main Content

### 1. Computer Program Design (Design_Computer_Programs)

#### 🧩 Classic Algorithm Problems (export_problem)
- **Bridge Problem** (`bridge_problem.py`) - Solving optimal bridge crossing time
- **River Crossing Problem** (`cross_river.py`) - River crossing strategy optimization
- **Missionaries and Cannibals Problem** (`missionaries_cannibals.py`) - Classic AI search problem
- **Water Pouring Problem** (`pour_problem.py`) - Solving jug capacity problems

#### 🔧 Tool Modules (tools)
- **JSON Parser** (`JSON_parser.py`) - JSON syntax parser implementation
- **Regular Expression Grammar** (`REGrammar.py`) - Regular expression syntax parsing
- **Math Language** (`MathLanguage.py`) - Mathematical expression processing
- **Memoization** (`Memoization.py`) - Performance optimization tool

#### 🎮 Probability Problems (probility_problem)
- **Conditional Probability** (`condictional_probility.py`) - Conditional probability calculation
- **Game Theory** (`game_theory.py`) - Game theory algorithms
- **Pig Dice Game** (`play_pig.py`, `play_pig_d.py`, `play_pig_optimal.py`) - Strategy optimization

### 2. Machine Learning Practice (housework)

#### 📊 Lesson 1: Machine Learning Basics
- **Linear Regression** (`linear_regression.py`) - House price prediction and other regression problems
- **Logistic Regression** (`logic_regression.py`) - Classification problem solving
- **MNIST Handwritten Digit Recognition** (`mnist_cart.py`) - Decision tree classification
- **Flight Delay Prediction** (`departure_prediction/`) - Time series prediction

#### 🔍 Lesson 2: Data Mining
- **Titanic Data Analysis** (`titanic/`) - Survival prediction analysis
- **Steam Video Games Data** (`steam_video_games/`) - Game data cleaning and analysis
- **Delicious Tags Clustering** (`delicious-2k/`) - Text clustering analysis
- **Team Clustering Analysis** (`team_cluster/`) - K-means clustering practice

#### 🛒 Lesson 3: Association Rule Mining
- **Market Basket Analysis** (`BreadBasket/`) - Apriori algorithm implementation
- **Movie Actor Association** (`MovieActors/`) - Association rule mining
- **Movie Recommendation** (`MovieLens/`) - Collaborative filtering algorithm
- **Market Basket Optimization** (`homework/MarketBasket.py`) - Purchase behavior analysis

#### 🌐 Lesson 4: Network Analysis
- **PageRank Algorithm** (`pagerank/`) - Web page importance ranking
- **TextRank Algorithm** (`textrank/`) - Text summarization extraction
- **Shortest Path** (`shortest_path/`) - Floyd algorithm implementation
- **Epidemic Data Analysis** (`EDA/`) - COVID-19 data exploration

## 🚀 Quick Start

### Requirements

```bash
Python >= 3.7
pip install -r requirements.txt
```

Main dependencies:
- `numpy` - Numerical computing
- `pandas` - Data processing
- `scikit-learn` - Machine learning
- `matplotlib` - Data visualization
- `tensorflow/keras` - Deep learning
- `networkx` - Network analysis

### Running Examples

#### 1. Run Classic Algorithm Problems
```bash
cd RS/Design_Computer_Programs/export_problem/
python bridge_problem.py
```

#### 2. Machine Learning Cases
```bash
cd RS/housework/lesson01/
python linear_regression.py
```

#### 3. MNIST Handwritten Digit Recognition
```bash
python mnist_keras.py
# or
python mnist_lr.py
```

## 📚 Learning Path

### Beginners
1. Start with basic algorithms in `Design_Computer_Programs/export_problem/`
2. Learn machine learning basics in `housework/lesson01/`
3. Practice with the `titanic/` data analysis case

### Intermediate
1. Deep dive into association rule mining in `lesson03/`
2. Explore network analysis algorithms in `lesson04/`
3. Study specific implementations of recommendation systems

### Advanced
1. Combine multiple modules to implement complete recommendation systems
2. Optimize algorithm performance and accuracy
3. Extend to real business scenarios

## 🔍 Key Features

- **Complete Learning System** - From basic algorithms to advanced applications
- **Practice-Oriented** - Real datasets and business scenarios
- **High Code Quality** - Detailed comments and test cases
- **Rich Algorithms** - Covers machine learning, data mining, network analysis, etc.
- **Highly Extensible** - Modular design, easy to extend

## 📖 Main Algorithms

### Machine Learning Algorithms
- Linear Regression
- Logistic Regression
- Decision Tree
- K-means Clustering

### Recommendation System Algorithms
- Collaborative Filtering
- Content Similarity Calculation
- Association Rule Mining (Apriori)

### Network Analysis Algorithms
- PageRank Algorithm
- TextRank Algorithm
- Shortest Path Algorithm (Floyd)

### Search Algorithms
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- State Space Search

## 🤝 Contributing

Issues and Pull Requests are welcome to improve this project!

## 📄 License

This project is for learning purposes only.

## 📞 Contact

For questions or suggestions, please contact via GitHub Issues.

---

*This is a comprehensive project for learning recommendation systems and machine learning algorithms, suitable for computer science students and developers interested in recommendation systems.*
