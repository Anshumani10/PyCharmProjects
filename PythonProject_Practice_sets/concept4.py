import pytest


@pytest.fixture
def sample_data():
    print("\n setup: creating test data")
    data = {"name" : "Alice", "age" : 30}
    yield data  #provides data to the test
    print("\n teardown: creating test data")


def test_exampleData(sample_data):

    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print("Test executed successfully")

