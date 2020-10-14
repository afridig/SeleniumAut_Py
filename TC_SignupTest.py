import unittest

class SignupTest(unittest.TestCase):
    def test_signUpByEmail(self):
        print("This is sign up by email test")
        self.assertTrue(True)

    def test_signUpByFacebook(self):
        print("This is sign up by facebook test")
        self.assertTrue(True)

    def test_signUpByTwitter(self):
        print("This is sign up by twitter test")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()