#any pytest should start with test_ or it can end with _test
#pytest method names should start with test keyword
#any code should wrap in method
import pytest


def test_firstProgram():
    print('hello world')

def test_secondProgram(setup):
    print("good bye")


@pytest.mark.smoke
def test_thirdProgram():
    msg = "night"
    assert msg == "hi", "test did not passed as the two strings not matched"

    
