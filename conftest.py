# file with GLOBAL fixtures should have name "conftest" only
# program has access to fixtures from same directory
import pytest


@pytest.fixture(scope="session")  # all tests will be run in one browser session
def browser():
    print("Browser fixture")
    yield  # go to body of test
    print("Close browser")