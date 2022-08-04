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

#### create dataframe ####
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

#other为多个DataFrame组成的列表时，只能实现index对index的匹配，这个时候不能设置on参数
#而且df2和df3中不能有相同的column
r3=df1.join([df2.set_index('Name'),df3.set_index('Name')],on='Name',how='outer')

################## Join ##################

#### create dataframe ####
df1=pd.DataFrame({'No.':range(1000,1004),
                  'Name':['July','Shiely','Lucy','Lily'],
                  'Salary':[5000,6000,4000,6000]})
df2=pd.DataFrame({'No.':range(1000,1005),
                  'Postion':['Manger','BOSS','BOSS','Manger','Manger'],
                  'Name':['July','Shiely','Lucy','Lily','Joy'],
                  'Bounce':[3000,1000,1000,2000,5000]})

#如果df2中的有多层索引时，需要都出现在on条件中才能正确进行匹配
r4=df1.join(df2.set_index(['No.','Name']),on=['No.','Name'],how='inner')
#如果没有设置lsuffix或rsuffix则会报错
r5=df1.join(df2,lsuffix='_left',how='inner')


################## Merge ##################

#### create dataframe ####
df1=pd.DataFrame({'Name':['July','Shiely','Lucy','Lily'],'Salary':[5000,6000,4000,6000]})
df2=pd.DataFrame({'Name':['July','Shiely','Lucy','Joy','Lily'],'Major':['CS','CS','Art','Art','Math']})
df3=pd.DataFrame({'Name':['July','Shiely','Lucy','Lily','Kate'],
                  'University':['Beking','Beking','Tsing','Tsing','SHU']})
df4=pd.DataFrame({'No.':range(1000,1004),
                  'Name':['July','Shiely','Lucy','Lily'],
                  'Salary':[5000,6000,4000,6000]})
df5=pd.DataFrame({'No.':range(1000,1005),
                  'Postion':['Manger','BOSS','BOSS','Manger','Manger'],
                  'Name':['July','Shiely','Lucy','Lily','Joy'],
                  'Bounce':[3000,1000,1000,2000,5000]})

### after merge only one col 'Name'
#df1.merge(df2,on='Name')

### col-index merge, result only has one col 'Name'
#r1=df1.merge(df2.set_index('Name'),left_on='Name',right_index=True)

#col-index join, must have on
#r1=df1.join(df2.set_index('Name'),how='inner',on='Name')

# index-index join, no need on
r1=df1.set_index('Name').join(df2.set_index('Name'),how='inner')
print(r1)

r2=df2.merge(df3,how='outer',indicator='source',validate='one_to_one')

r3=df4.merge(df5,on='No.',suffixes=('_left','_right'))
r4=df1.set_index('Name').merge(df2.set_index('Name'),left_index=True,right_index=True)


################## Concat ##################

se1=pd.Series(['July','Shiely','Lucy','Lily'])
se2=pd.Series([5000,6000,4000,6000],index=range(1000,1004))
r1=pd.concat({'name':se1,'salary':se2},axis=0,join='outer')
#se1和se2也可以放在list或tuple里
r2=pd.concat({'name':se1,'salary':se2},axis=0,join='outer',ignore_index=True)
#使用dict进行数据传输的时候，字典的键会作为外层索引的名字或列名
#所以这里series.name可以为None
#使用了ignore_index之后，会重新给返回结果设置索引
df1=pd.DataFrame({'Name':['July','Shiely','Lucy','Lily'],'Salary':[5000,6000,4000,6000]},index=range(1000,1004))
df2=pd.DataFrame({'Name':['July','Shiely','Lucy','Joy','Lily'],'Major':['CS','CS','Art','Art','Math']},
                index=range(1000,1005))
r3=pd.concat((df1,df2),axis=0,join='inner',sort=False)
#join作用，当axis=0时，则只保留两个待合并元素中的相同column
#当axis=1时，则只保留两个待合并元素中的相同index
r4=pd.concat((df1,df2),axis=1,join='inner',sort=False)
r5=pd.concat([df1,se1,se2,df2],axis=1,join='outer')
