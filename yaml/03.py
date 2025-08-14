
import os
import yaml

def write_yam(yaml_path, data):
    """ yaml单个数据写入 """
    if not os.path.isfile(yaml_path):
        raise FileNotFoundError(f"文件路径不存在, {yaml_path}")
    
    if not isinstance(data, list):
        raise TypeError(f"data参数必须是列表, 现在类型是{type(data)}")
    
    # 写入yaml文件
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)
    
def write_yam_group(yaml_path, data):
    """ yaml多个数据写入 """
    if not os.path.isfile(yaml_path):
        raise FileNotFoundError(f"文件路径不存在, {yaml_path}")
    
    if not isinstance(data, list):
        raise TypeError(f"data参数必须是列表, 现在类型是{type(data)}")
    
    # 写入yaml文件
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump_all(documents=data, stream=f, allow_unicode=True)



if __name__ == "__main__":

    list_data = [
    {'username': 'user1', 'password': 'psw1'}, 
    {'username': 'user2', 'password': 'psw2'},
    {'username': 'user3', 'password': 'psw3'}, 
    {'username': 'user4', 'password': 'psw4'}, 
    {'username': 'user5', 'password': 'psw5'}
    ]

    path = r"D:\2_python_file\pytest_test\03.yaml"

    write_yam(yaml_path=path, data=list_data)