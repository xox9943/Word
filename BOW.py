import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer()
# 语料库
#两篇文档
docs = np.array([
    "Where there is a will, there is a way.",
    "There is no royal road to learning.",
])
bag = count.fit_transform(docs)
# 输出单词与编号的映射关系。
print(count.vocabulary_)  # 某个单词的数字表示
print(count.get_feature_names())  # 按照数字顺序，输出key单词
# 其中，value的数字是按照字典序a-z来排序的。

# 调用稀疏矩阵的toarray方法，将稀疏矩阵转换为ndarray对象。
print(bag)  # 第i篇，的某个单词表示的数字，该单词在第i篇中的出现次数。
print(bag.toarray())

# where映射为编号8  there映射为编号5······
# 编号也是bag.toarray转换来的ndarray数组的索引
import
