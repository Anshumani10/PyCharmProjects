import pytest
#@pytest.fixture()
#def setup():
    #print("This will executed first")
    #yield
    #print("I will be executed last")

@pytest.mark.usefixtures("setup")
class TestExamples:
    def test_fixturedemo(self):
        print("I will execute steps in fixture demo")

    def test_fixturedemo1(self):
        print("I will execute steps in fixture demo")

    def test_fixturedemo2(self):
        print("I will execute steps in fixture demo")

    def test_fixturedemo3(self):
        print("I will execute steps in fixture demo")

