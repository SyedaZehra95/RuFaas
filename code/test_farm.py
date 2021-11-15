import unittest
import unittest.mock as mock
from src import pen
from src import farm
class TestPen(unittest.TestCase):
    def __init__(self, methodName: str = ...,) -> None:
        super().__init__(methodName=methodName)

    def test_get_pen(self):
        f=farm.Farm()
        self.assertEqual(f.getPenCount(),0,"Should return 0")
    
    def test_createPen1(self):
        f=farm.Farm()
        p=pen.Pen("A",1,3)
        self.assertEqual(f.createPen("A",p),True,"Should creat pen for breed A as it doesnt exist ")
    
    def test_createPen2(self):
        f=farm.Farm()
        p=pen.Pen("A",1,3)
        f.createPen("A",p)
        self.assertEqual(f.createPen("A",p),False,"Should return False since pen for breed A is already created")
    
    def test_checkBreed1(self):
        f=farm.Farm()
        p=pen.Pen("A",1,3)
        f.createPen("A",p)
        self.assertEqual(f.checkBreed("A"),True,"Should return True as pen for breed A exist")
    
    def test_checkBreed2(self):
        f=farm.Farm()
        p=pen.Pen("A",1,3)
        f.createPen("B",p)
        self.assertEqual(f.checkBreed("B"),False,"Should return False as pen for breed B doesnt exist")
    
    

if __name__ == '__main__':
    unittest.main()