#assertIn & assertNotIn

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list={"python","selenium","java"}

        #self.assertIn("python",list) #positive condition, positive test

        #self.assertIn("ruby",list ) #neagtive test passes as this will return FALSE
        #self.assertNotIn("python",list) #failed -->this will return a FALSE value as the value inside the parenthesis is TRUE
        self.assertNotIn("ruby",list) #passed -->this will return a TRUE value as the value inside the parenthesis is FALSE

if __name__ == "__main__":
    unittest.main()