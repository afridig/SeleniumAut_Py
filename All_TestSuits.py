import unittest

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#get all tests from LoginTest, SignUpTest, PaymentTest and PaymentReturnsTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#creating test suits
sanityTestSuite=unittest.TestSuite([tc1,tc2]) #Sanity test suite (this contains only basic signup and login functionality)
functionalTestSuite=unittest.TestSuite([tc3,tc4]) #Functional test suite (this contains functionality tests)
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4]) #Master test suite (this contains all the tests encompassing sanity as well as functional tests)

#unittest.TextTestRunner().run(sanityTestSuite) #running sanity test suite
#unittest.TextTestRunner().run(functionalTestSuite) #running functionality test suite

unittest.TextTestRunner(verbosity=2).run(masterTestSuite) #running all tests contained in both sanity and functionality
