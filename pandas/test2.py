"""
返回格式,列表套字典 
[{"ID": 1, "用户名": "user01", "密码": "psw01", "地址":"北京01"}] 
"""

import pandas as pd
import pathlib
import pytest

excel_path = pathlib.Path(__file__).parent.absolute() / "01.xlsx"


def write_excel(file_path, data, sheet_name="Sheet1"):
    """ 写入数据excel """
    df = pd.DataFrame(data)

    # 追加 这样才能增加sheet页
    # 如果有同名的sheet页，先删除再写入
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writre:

        # 删除sheet页，如果存在
        if sheet_name in writre.book.sheetnames:
            writre.book.remove(writre.book[sheet_name])
        
        # 写入数据
        df.to_excel(writre, sheet_name=sheet_name, index=False)


data_s = [
    {'ID': 11, '用户名': 'user01', '密码': 'psw01', '地址': '北京01'}, 
    {'ID': 22, '用户名': 'user02', '密码': 'psw02', '地址': '北京02'}, 
    {'ID': 33, '用户名': 'user03', '密码': 'psw03', '地址': '北京03'}, 
    {'ID': 44, '用户名': 'user04', '密码': 'psw04', '地址': '北京04'}, 
    {'ID': 55, '用户名': 'user05', '密码': 'psw05', '地址': '北京05'}]
data_ss = {
    'ID': [66, 77, 88, 99, 110],
    '用户名': ['user6', 'user7', 'user8', 'user9', 'user10'],
    '密码': ['psw6', 'psw7', 'psw8', 'psw9', 'psw10'],
    '地址': ['北京6', '北京7', '北京8', '北京9', '北京10']
}
write_excel(file_path=excel_path, data=data_s, sheet_name="Sheet1")


def dict_data(file_path, sheet_name="Sheet1"):
    """ 读取数据excel """
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

    # 列名
    header = df.columns.tolist()
    # 列数
    cols = df.shape[1]
    # 行数
    rows = df.shape[0]

    if rows == 0:
        raise Exception(f"{file_path} 文件没有数据")
    
    # # 方法一，直接factory转换 --> 列表套字典
    # data = df.to_dict('records') 

    # # 方法二，自定义转换缺失值
    # # .fillna("N/A") 填充缺失值 N/A
    # header = df.columns.tolist()
    # data = []
    # for i in range(len(df)):
    #     row_data = df.iloc[i].fillna("N/A").tolist()
    #     row_dict = dict(zip(header, row_data))
    #     data.append(row_dict)

    # 方法三，推荐使用
    # 把excel数据转换成字典，key为列名，value为列值
    data = df.fillna("N/A").to_dict('records')

    return data


datas = dict_data(file_path=excel_path, sheet_name="Sheet1")
print(datas)


# 测试类
class TestDemo(): 
    """ 测试类 使用excel数据驱动 """
    @pytest.mark.parametrize('data', datas)
    def test_login(self, data):
        print(f"输入ID, {data['ID']}")
        print(f"输入用户名， {data['用户名']}")
        print(f"输入密码， {data['密码']}")
        print(f"输入地址， {data['地址']}")
        print(f"点击登录")
        assert 1 == 1

        