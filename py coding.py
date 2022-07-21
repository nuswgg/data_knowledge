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

###### Merge Concat ######
##########################

# a dictionary to convert to a dataframe
data1 = {'identification': ['a', 'b', 'c', 'd'],
'Customer_Name':['King', 'West', 'Adams', 'Mercy'], 'Category':['furniture', 'Office Supplies', 'Technology', 'R_materials'],}

# our second dictionary to convert to a dataframe
data2 = {'identification': ['a', 'b', 'c', 'd'],
'Class':['First_Class', 'Second_Class', 'Same_day', 'Standard Class'],
'Age':[60, 30, 40, 50]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# using .merge() function
new_data = pd.merge(df1, df2, on='identification')
#print(new_data)

# y轴concat 相当于append
ndata = pd.concat([df1,df2],axis=0)
#print(ndata)

#  和merge能达到一样的效果
nndata = pd.concat([df1,df2],axis=1)
print(nndata)


df1=pd.DataFrame({'Name':['July','Shiely','Lucy','Lily'],'Salary':[5000,6000,4000,6000]})
ser1=pd.Series(['US','CN','UK','UK'],index=['July','Shiely','Lucy','Lily'],name='Nation')
df2=pd.DataFrame({'Name':['July','Shiely','Lucy','Joy','Lily'],'Major':['CS','CS','Art','Art','Math']})
df3=pd.DataFrame({'Name':['July','Shiely','Lucy','Lily','Joy'],
                  'University':['Beking','Beking','Tsing','Tsing','Beking']})

# print(df1)
# print(df2)
# print(df3)
# print(ser1)

#用df1.Name字段和Ser1.index匹配
r1=df1.join(ser1,how='inner',on='Name')

#这里是将Name属性都设为df1和df2的索引然后再进行匹配连接的。这时候就不用写on条件了，
#同时df1和df2中的Name顺序不一致也可以正常处理。
#同时sort字段实现了按name的字典序重新排序
r2=df1.set_index('Name').join(df2.set_index('Name'),how='inner',sort=True)

