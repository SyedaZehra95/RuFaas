class Pen:
    def __init__(self,breed:str, capacity:int,cost_per_serving:int ):
        self.breed = breed
        self.capacity = capacity
        self.number_of_cows = 0
        self.cost_per_serving=cost_per_serving
    
    def getBreed(self):
        return self.breed
    
    def getCapacity(self):
        return self.capacity
    
    def getNumberOfCows(self):
        return self.number_of_cows

    def addCow(self,breed:str):
        if (self.breed == breed )and self.number_of_cows <self.capacity:
            self.number_of_cows=self.number_of_cows+1
            return True
        return False

    def addCows(self,breed:str,val:int):
        if (self.breed == breed )and (self.number_of_cows + val ) <= self.capacity:
            self.number_of_cows=self.number_of_cows+val
            return True
        return False

    
    def getMilk(self, days):
        return days*self.number_of_cows
    
    def getCost(self,days):
        return days * self.number_of_cows * self.cost_per_serving
    
    def getRemainingCapacity(self):
        return self.capacity-self.number_of_cows
    
'''p=Pen("A",1,3)
print(p.getBreed())
print(p.addCow("A"))
print(p.getNumberOfCows())
print(p.addCow("A"))'''
    


    
