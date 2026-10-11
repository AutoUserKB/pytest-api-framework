import pytest

@pytest.fixture
def base_url():
    base_url = "https://jsonplaceholder.typicode.com/users"
    return base_url

@pytest.fixture
def demo():
    print("\nFixture Running")
    return 1