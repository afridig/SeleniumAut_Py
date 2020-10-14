import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentInDollers(self):
        print("This is payment in dollers test.")
        self.assertTrue(True)

    def test_paymentInRupees(self):
        print("This is payment in rupees test.")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
