import unittest
from player import Player
from HourlyEmployee import HourlyEmployee
from salaried_employee import SalariedEmployee
#write import statements for required classes or functions

class TestFinalExam(unittest.TestCase):
    #3 points
    #Create a test case to test the non_contiguous_motif  function with values
    #['A', 'C','G','T','A','C','G','T','G','A','C','G'] that returns three values 3, 8, and 10
    def test_non_contigous_motif(self):
        self.assertEqual((2,5,9), ['T', 'A','T','G','C','T','A','A','G','A','T','C'])
    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values True, 8, and 9 the result should be 'Invalid range'
    def test_check_come_out_roll_8_9(self):
        p = Player(8,9)
        self.assertEqual('Invalid Range',p.check_come_out_roll())

    def test_check_come_out_roll_4_7(self):
        p = Player(4,7)
        self.assertEqual('Loser',p.check_come_out_roll())
       #3 points
    #Add a test case for HourlyEmployee that calls the calculate method with values 10 and 80 to yield a result of 800.
    def test_HourlyEmployee(self):
        p = HourlyEmployee(1,'bob',10,80)
        self.assertEqual(800, p.calculate())
    #3 points
    #Add a test case for SalariedEmployee that calls the calculate method with values 260000 to yield a result of 10000.

    def test_salariedEmployee(self):
        p = SalariedEmployee(1,'bob',260000)
        self.assertEqual(10000,p.calculate())
    

    

unittest.main(verbosity=2)       
