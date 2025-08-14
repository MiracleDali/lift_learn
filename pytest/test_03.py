import pytest

class TestCase():

    def setup(self):
        print("这是不在类中的前置")

    def teardown(self):
        print("这是不在类中的后置")   

    def test_case01(self):
        num = 1+1
        assert num == 2, "断言失败：1+1不等于2"
        print("断言成功: 1+1等于2")
    @pytest.mark.usefixtures('init_function')
    
    def test_case02(self):
        num = 1+2
        assert num == 3, "断言失败：1+1不等于3"
        print("断言成功：1+1等于3")