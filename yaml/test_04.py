import pytest
import yaml
import pathlib

yamlpath = pathlib.Path(__file__).parent.absolute() / "04.yaml"


def read_yaml(yamlpath):
    """ 读取yaml文件 """
    with open(yamlpath, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
    
case_data = read_yaml(yamlpath)


class TestDemo(): 
    @pytest.mark.parametrize('data', case_data)
    def test_login(self, data):
        print(f"输入用户名， {data['用户名']}")
        print(f"输入密码， {data['密码']}")
        print(f"点击登录")
        assert 1 == 1


        