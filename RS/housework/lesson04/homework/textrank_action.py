# -*- encoding: utf-8 -*-
from textrank4zh import TextRank4Keyword, TextRank4Sentence
from snownlp import SnowNLP

with open("news.txt", "r", encoding='utf-8') as f:  # 打开文件
    text = f.read()  # 读取文件
    print(text)

text4w = TextRank4Keyword()
text4w.analyze(text, window=2, lower=True)
print('关键字：')
# 输出结果缺少开学关键字
for word in text4w.get_keywords(num=10):
    print(word)
text4s = TextRank4Sentence()
text4s.analyze(text, lower=True )
print('摘要：')
for sentence in text4s.get_key_sentences(num=3):
    print(sentence)

# nlp  能有开学的关键字
# sp = SnowNLP(text)
# print(sp.keywords(10))
# print(sp.summary(10))

