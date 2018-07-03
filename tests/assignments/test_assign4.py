import unittest

from src.assignments.assignment4 import factorial

class Test_Assign4(unittest.TestCase):

    def test_factorial_w_value_5(self):
        '''
        This is an example to guide you in creating test cases.
        The sample_function takes an argument and returns the same value. If it takes a 2 it will return a 2.
        :return:
        '''
        self.assertEqual(120, factorial(5))

    def test_factorial_w_value_6(self):
        '''
        This is an example to guide you in creating test cases.
        The sample_function takes an argument and returns the same value. If it takes a 2 it will return a 2.
        In this test case, the test is for no equality.
        :return:
        '''
        self.assertEqual (720, factorial(6))

#create two test cases for the factorial function, one test case with a value of 5 and the other with value of 6
#THE NAME OF THE FUNCTION MUST BEGIN WITH test OTHERWISE THE TestCase suite will not recognize it as a test case.





#remove the pound sign at the beginning of the next statement to run tests locally.
if __name__ == '__main__':
    unittest.main(verbosity=4)
#add the pound sign back before uploading to Github

