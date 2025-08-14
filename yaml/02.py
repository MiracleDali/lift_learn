
import yaml
from string import Template
import os

def yaml_template(yamlpath, change_data):
    """ yaml变量的动态替换 """
    # 判断文件是否存在
    if not os.path.isfile(yamlpath):
        raise FileNotFoundError(f"文件路径不存在, {yamlpath}")
    
    # 判断参数类型
    if not isinstance(change_data, dict):
        raise TypeError("change_data参数必须是字典")
    
    # 读取yaml文件内容
    with open(yamlpath, "r", encoding="utf-8") as f:
        cfg = f.read()
    # 动态替换
    content = Template(cfg).substitute(**change_data)
    # 加载成yaml对象并返回
    return yaml.load(content, Loader=yaml.FullLoader)




if __name__ == "__main__":
    path = r"D:\2_python_file\pytest_test\02.yaml"
    data = {
        "user": "admin", 
        "pass": "123456"
    }
    content = yaml_template(yamlpath = path, change_data = data)
    print(content)