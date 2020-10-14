import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest #skip test by the decorator method
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test method because it is not yet ready.") #skipping test by sepcifying reason through the decorator
    def test_advancedSearch(self):
        print("This is advanced search")

    @unittest.skipIf(1==1,"Numbers are not equal.")
    def test_prepaidRecharge(self):
        print("This is pre-paid recharge")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge")

    def test_loginByGmail(self):
        print("This is login by email test")

    def test_loginByTwitter(self):
        print("This is login by twitter test")

if __name__ == "__main__":
    unittest.main