from pen import Pen

class Farm:
    def __init__(self) -> None:
        self.pen_count=0
        self.breed_pen={}
    
    def getPen(self,breed_name:str):
        if breed_name in self.breed_pen:
            return self.breed_pen[breed_name]
        return False
    def getPenCount(self):
        return self.pen_count
    
    def updatePenCount(self):
        self.pen_count+=1

    def checkBreed(self, breed:str):
        return  breed in self.breed_pen
        
    def createPen(self,breed:str,pen:Pen):
        if breed in self.breed_pen:
            return False
        else:
            self.breed_pen[breed]=pen
            self.updatePenCount()
            return True