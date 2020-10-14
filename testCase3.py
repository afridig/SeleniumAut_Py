import unittest

def setUpModule(): #this method will be executed before executing any class or any method present in the test class
    print("setUpModule")

def tearDownModule(): #this metod will be executed after completing everything present in the python module
    print("tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is a login test") #this method will execute once before each and every method present in the class

    @classmethod
    def tearDown(self):
        print("This is a logout test") #this method will execute once after each and every method present in the class

    @classmethod
    def setUpClass(cls):
        print("Opens application") #setUpClass will execute once, when it will open the application

    @classmethod
    def tearDownClass(cls):
        print("Closes the application") #tearDownClass will execute once, after the class is executed, when it will close the application

    def test_search(self):
        print("This is a search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is a prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is a postpaid Recharge test")

if __name__ == "__main__":
    unittest.main()