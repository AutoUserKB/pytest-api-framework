import pytest
import requests

@pytest.fixture
def base_url():
    base_url = "https://jsonplaceholder.typicode.com"
    return base_url

@pytest.fixture(scope="session")
def demo():
    print("\nFixture Running")
    return 1

@pytest.fixture(scope="class")
def setup_data():
    print("\nclass setup")
    return 1




