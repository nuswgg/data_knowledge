import pandas as pd
import numpy as np

# 创建dataframe
# coords = [("AA", "one"), ("AA", "six"), ("BB", "one"), ("BB", "two"), ("BB", "six")]
# index = pd.MultiIndex.from_tuples(coords)
# df = pd.DataFrame([11, 22, 33, 44, 55], index, ["MyData"])

# # 多层index，对level 0进行筛选
# print(df.xs('AA',level=0,axis=0))

# # 多层index，对level 1进行筛选
# print(df.xs('six',level=1,axis=0))

# # 多层index，对单行进行筛选
# print(df.xs(('AA','one')))

# 创建dataframe
# arrays = [['one','one','one','two','two','two'],[1,2,3,1,2,3]]
# df = pd.DataFrame(np.random.randn(6,2),index=pd.MultiIndex.from_tuples(list(zip(*arrays))),columns=['A','B'])
#print(df)

#多层index，对level 0进行筛选
#print(df.xs('one'))

#多层index，对单列进行筛选
#print(df.xs('A',axis=1))

#多层index，对双列进行筛选
#print(df.xs(['A','B'],axis=1))

#多层index，对单行进行筛选
#print(df.xs(('one',1)))

#多层index，对单个元素进行筛选
#print(df.xs(('one',1)).A)

#多层index，对多个元素进行筛选
#print(df.xs(('one',1)).loc[['A','B']])

cols = pd.MultiIndex.from_tuples(
    [(x, y) for x in ["A", "B", "C"] for y in ["O", "I"]]
)
df = pd.DataFrame(np.random.randn(2, 6), index=["n", "m"], columns=cols)
print(df)
df1 = df.div(df["C"], level=1)
print(df1)


