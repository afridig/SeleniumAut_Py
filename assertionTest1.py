import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebpage=driver.title
        #assertEqual----> this will check if the two values are equal, if TRUE, the test passes, otherwise it fails
        self.assertEqual("Google",titleOfWebpage,"title of the webpage is not the same as expected") #positive test with positive condition
        #following is a negative test
        #self.assertEqual("Google123",titleOfWebpage,"title of the webpage is not the same as expected")

        #positive test with a negative condition
        #self.assertNotEqual("Google",titleOfWebpage)
        #nagative test with a negative condition
        #self.assertNotEqual("Google123",titleOfWebpage)

if __name__ == "__main__":
    unittest.main()
