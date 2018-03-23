import unittest
from src.homework.homework7 import pdistance, pdistance_matrix

#write import statement for homework 7 file


class TestHomework7(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    def test_pdistance(self):
        self.assertEqual(['0.00000', '0.40000', '0.10000', '0.10000', 
                           '0.40000','0.00000', '0.40000', '0.30000',
                           '0.10000', '0.40000', '0.00000', '0.20000',
                           '0.10000', '0.30000', '0.20000', '0.00000'], pdistance_matrix([
     ['T','T','T','C','C','A','T','T','T','A'],
     ['G','A','T','T','C','A','T','T','T','C'],
     ['T','T','T','C','C','A','T','T','T','T'],
     ['G','T','T','C','C','A','T','T','T','A']
    ]))

    #create a test for get p distance matrix with following data
    '''
    Sample Dataset
    [
     ['T','T','T','C','C','A','T','T','T','A'],
     ['G','A','T','T','C','A','T','T','T','C'],
     ['T','T','T','C','C','A','T','T','T','T'],
     ['G','T','T','C','C','A','T','T','T','A']
    ]
    
    Sample Output
    0.00000 0.40000 0.10000 0.10000
    0.40000 0.00000 0.40000 0.30000
    0.10000 0.40000 0.00000 0.20000
    0.10000 0.30000 0.20000 0.00000
    '''
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
