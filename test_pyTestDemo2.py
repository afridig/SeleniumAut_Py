import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method.")
    yield
    print("Once after every method.")


def testMethod1(setup):
    print("This is test method 1.")


def testMethod2(setup):
    print("This is test method 2.")

#def testMethod2():  #this method doesn't have setup keyword included so the fixture method wont be executed before this method
    #print("This is test method 2.")
