import unittest
import cube_volume

class TestCubeVolume(unittest.TestCase):
    def test_cube_volume_int(self):
        result1 = cube_volume.cube_volume(5, 2, 3)
        self.assertEqual(result1, 30)
    
    def test_cube_volume_float(self):
        result2 = cube_volume.cube_volume(5.5 ,3.2, 6.4)
        #actual computed value is 112.64000000000001
        self.assertAlmostEqual(result2, 112.64)
        self.assertEqual("{:0.2f}".format(result2), "112.64")
    
    def test_cube_volume_args(self):
        err_string = "TypeError, non numbers were entered"
        result3 = cube_volume.cube_volume("a", "b", [])
        self.assertEqual(result3, err_string)

if __name__ == '__main__':
    unittest.main()