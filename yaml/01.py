

import os
import yaml

def read_yaml(yamlpath):
    """ 读取yaml文件 """
    # 判断文件是否存在
    if not os.path.isfile(yamlpath):
        raise FileNotFoundError("文件不存在")
    
    # 读取文件
    with open(yamlpath, "r", encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        return content
    

def read_yaml_group(yamlpath):
    """ 读取yaml文件组 """
    # 判断文件是否存在
    if not os.path.isfile(yamlpath):
        raise FileNotFoundError("文件不存在")
    
    with open(yamlpath, "r", encoding="utf-8") as f:
        # 先把yanl文件内容加载到一个变量中
        cfg = f.read()   
    # 把变量加载成yaml对象
    content = yaml.load_all(cfg, Loader=yaml.FullLoader)
    return content   
    

    
if __name__ == "__main__":
    content = read_yaml_group(yamlpath=r"D:\2_python_file\pytest_test\02.yaml")
    print(content)
    for i in content:
        print(i)


