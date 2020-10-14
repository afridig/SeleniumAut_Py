import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to sign up.")
    yield
    print("Closing browser after sign up.")

def test_signUpByEmail(setUp):
    print("This is sign up by email test.")

def test_signUpByFacebook(setUp):
    print("This is sign up by facebook test.")
