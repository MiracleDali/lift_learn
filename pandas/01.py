import pandas as pd
import pathlib


# 获取文件绝对路径
excel_path = pathlib.Path(__file__).parent.absolute() / "01.xlsx"


""" 读取excel文件内容 """
# header=0 表示第一行是列名
# index_col='ID' 表示ID列作为索引
# dtype=None 表示不转换数据类型   dtype={'用户名': str} 表示用户名列转换成字符串类型
df = pd.read_excel(excel_path, sheet_name="Sheet1", header=0, index_col='ID', dtype=None)
print("内容:\n", df)


""" 获取所有sheet名 """
# .keys() 获取所有sheet名
# .values() 获取所有sheet内容
sheet_names = pd.read_excel(excel_path, sheet_name=None).keys()
print("\n列名:", list(sheet_names))


""" 
行的操作 
header=None 表示第一行不是列名当成普通列
.shape[0] 获取行数
.iloc[索引] 获取行数据
.loc[标签] 获取行数据
"""
df = pd.read_excel(excel_path, sheet_name="Sheet1", header=0, index_col='ID', dtype=None)
print("\n行数:", df.shape[0])
# 根据位置索引获取单行数据 返回一个Series 一维数组
print("\n根据位置索引获取行数据:\n", df.iloc[1])
print("\n两个中括号可以取到对应行的指定列内容:\n", df.iloc[1][['用户名', '地址']])

# 根据标签索引获取单行数据 
print("\n根据标签索引获取行数据:\n", df.loc[5])
print("\n两个中括号可以取到对应行的指定列内容:\n", df.loc[5][['用户名', '地址']])

# 根据标签索引获取多行数据 
print("\n读出多行数据:\n", df.loc[5:6])
print("\n两个中括号可以取到对应行的指定列内容:\n", df.loc[5:6][['用户名', '地址']])


""" 
列的操作 
.shape[1] 获取列数
.columns 获取列名
.iloc[:, 索引] 获取列数据
.loc[:, 标签] 获取列数据
"""
df = pd.read_excel(excel_path, sheet_name="Sheet1", header=0, index_col='ID', dtype=None)
print("\n列数:", df.shape[1])
print("列名:", df.columns)

print("\n获取单列数据:\n", df['地址'])
print("\n获取单列数据上的某个数据:\n", df['地址'][7])

print("\n获取多列数据:\n", df[['用户名', '地址']])
print("\n获取多列数据上的某个数据:\n", df[['用户名', '地址']].loc[5])

print("\n获取多列数据:\n", df.iloc[:, [1]])



