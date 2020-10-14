import pytest

@pytest.fixture() #this makes sure that the method decorate here is run once before every method
def setup():      #that follows this and has setup keyword enclosed in parenthesis
    print("Once before every method")

def testMethod1(setup):
    print("This is test method 1.")

def testMethod2(setup):
    print("This is test method 2.")

#def testMethod2():  #this method doesn't have setup keyword included so the fixture method wont be executed before this method
    #print("This is test method 2.")
    