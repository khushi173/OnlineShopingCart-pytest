import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("Open amazon app")
    print("user logged in ")
    yield
    print("logged out")
    print("closed amazon app")