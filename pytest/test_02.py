import pytest

class TestCase:

    test_data = [{"uesr_name": "xiaoming", "password": "123456"}, {"uesr_name": "xiaoming1", "password": "1234561"},
                  {"uesr_name": "xiaoming2", "password": "1234562"}, {"uesr_name": "xiaoming3", "password": "1234563"}]
    @pytest.mark.parametrize("casedata", test_data, ids=["case1", "case2", "case3", "case4"])
    def test_01(self, casedata):
        print(f"输入用户名 {casedata['uesr_name']}")
        print(f"输入密码 {casedata['password']}")
        assert "登录成功" == "登录成功"




