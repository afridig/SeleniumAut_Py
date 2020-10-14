#relational comparisons

#assertGreater
import unittest

class Test(unittest.TestCase):
    def testName(self):
        #self.assertGreater(100,10) #positive test --> test passes
        #self.assertGreater(10,100) #negative test --> test fails

        #assertGreaterEqual
        #self.assertGreaterEqual(100,10) #this will return TRUE and pass the test --> positive test
        #self.assertGreaterEqual(100,100) #this will return TRUE and pass the test --> positive test
        #self.assertGreaterEqual(10,100) #this will return a FALSE value and fail the test --> negative test

        #assertLess
        #self.assertLess(10,100) #this will return TRUE and pass the test
        #self.assertLess(100,10) #this will return FALSE and fail the test

        #assertLessEqual
        #self.assertLessEqual(100,100) #this will return TRUE and pass the test as the condition in the parentesis returns TRUE
        self.assertLessEqual(10,100) #TRUE -->passed test


if __name__ == "__main__":
    unittest.main()


