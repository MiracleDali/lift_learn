import pytest


class Test01:

    @pytest.mark.usefixtures("session_scope_fixture")
    def test_01(self, session_scope_fixture):
        print(session_scope_fixture)
        print("我是用例1")
        assert 1 == 1

    @pytest.mark.parametrize("param", [1, 2, 3])
    def test_02(self, param):
        print(param)
        print("我是用例2")
        assert 1 == 1