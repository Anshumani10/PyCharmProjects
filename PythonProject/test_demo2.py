#-k stands for method execution
# -s stands for logs output
#-v stands for more info
# you can mark <tag> any method which you want to run by -m
#fixtures are used as setup and teardown method for test cases -conftest file to generalize fixture
#fixture and make it available to all test cases.

import pytest


@pytest.mark.smoke
#@pytest.mark.skip
def test_thirdProgram():
    msg = "day"
    assert msg == "day", "test did not passed as the two strings not matched"
@pytest.mark.skip
def test_CreditCard():
    a=4
    b=6
    assert a+2 == b, "Addition do not match"

@pytest.mark.xfail
def test_Greeting():
    msg = "Hello"
    print("Yo it works!")

@pytest.fixture()
def setup():
    print("This will executed first")

def test_fixturedemo(setup):
    print("I will execute steps in fixture demo")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])







