import unittest
import unittest.mock as mock
from src import pen
class TestPen(unittest.TestCase):
    def __init__(self, methodName: str = ...,) -> None:
        super().__init__(methodName=methodName)

    def test_breed(self):
        p=pen.Pen("A",1,4)
        self.assertEqual(p.getBreed(), "A", "Should be A")

    def test_add_cow1(self):
        p=pen.Pen("A",1,4)
        self.assertEqual(p.addCow("A"), True, "Should return True")

    def test_add_cowB(self):
        p=pen.Pen("A",1,4)
        self.assertEqual(p.addCow("B"), False, "Should return False")

    def test_number_of_cows(self):
        p=pen.Pen("A",1,4)
        p.addCow("A")
        self.assertEqual(p.getNumberOfCows(),1,"Should return 1")

    def test_add_cow2(self):
        p=pen.Pen("A",3,4)
        self.assertEqual(p.addCows("A",2), True, "Should return True")

    def test_add_cow3(self):
        p=pen.Pen("A",3,4)
        self.assertEqual(p.addCows("A",4), False, "Should return False")
    
    def test_number_of_cows1(self):
        p=pen.Pen("A",3,4)
        p.addCows("A",2)
        self.assertEqual(p.getNumberOfCows(),2,"Should return 2")
    
    def test_milk_estimate(self):
        p=pen.Pen("A",3,4)
        p.addCows("A",3)
        self.assertEqual(p.getMilk(3),9,"Should return 9")

if __name__ == '__main__':
    unittest.main()