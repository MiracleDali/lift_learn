import pytest


@pytest.fixture(scope="session",
                params=[1, 2, 3],
                ids=["one", "two", "three"])
def session_scope_fixture(request):
    print("session_scope_fixture")
    res = request.param
    yield res
    print("session_scope_fixture teardown")