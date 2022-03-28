import pytest

@pytest.fixture()
def setUp():
    print("Setup started")
    yield
    print("exited")

def test_AddItemtoCart(setUp):
    print("added successfully")

def test_RemoveItemFromCart(setUp):
    print("removed sucessfully")