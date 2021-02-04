import unittest
import avg_of_elems

int_input_list = [5, 10, 15, 20, 33, 4]

float_input_list = [1.2, 3.5, 5.32, 6.77, 2.9]

class TestAvgOfElems(unittest.TestCase):
    def test_int_input(self):
        result1 = avg_of_elems.avg_of_elems(int_input_list)
        self.assertEqual(result1, 14.5)
    
    def test_float_input(self):
        result2 = avg_of_elems.avg_of_elems(float_input_list)
        #actual computed value is 3.9379999999999997
        self.assertEqual(result2, 3.9379999999999997)
        self.assertEqual("{:0.2f}".format(result2), "3.94")

    def test_empty_list(self):
        err_string = "The list is empty"
        result3 = avg_of_elems.avg_of_elems([])
        self.assertEqual(result3, err_string)




if __name__ == '__main__':
    unittest.main()