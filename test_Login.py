import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to Login")
    yield
    print("Closing browser after login")


def test_loginByEmail(setUp):
    print("This is login by email test.")

def test_loginByFacebook(setUp):
    print("This is login by facebook test.")

#to run just a specific module in the package --> pytest -v -s test_SignUp.py
#to run everything present in the package by specifying the path of the package --> pytest -v -s C:\Users\User\PycharmProjects\pythonWithSeleniumProject4\myPack
#to run just a specific method in a module, in the terminal --> pytest -v -s test_Login.py::test_loginByFacebook
