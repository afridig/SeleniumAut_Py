import pytest

def testMethod1():
    print("This is test method 1.")

def testMethod2():
    print("This is test method 2.")

#to run the above tests you have use the terminal where the console is
#use pytest command in the terminal to run the tests
#to run as well as get the print statements or whatever is in the display, you have to use pytest -v -s
#to just run a specific test in the module or in the package you have to specify the name of the test as follows
#pytest -v -s test_PyTestDemo.py