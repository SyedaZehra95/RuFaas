from farm import Farm
from pen import Pen

class Main:

    def __init__(self,farm:Farm) -> None:
        self.farm=farm
    def createPen(self):
        number_of_pens=int(input("\nEnter number of pens in the farm: \n"))
        i=1
        while i<=number_of_pens:
            breed_name=input("\n Enter breed of pen "+ str(i) + ": \n")
            if self.farm.checkBreed(breed_name):
                print("\n Pen of this breed exist. Please enter another breed name:\n")
                continue
            capacity = int(input("\n Enter the capacity of pen "+str(i)+"\n"))
            cost_per_serving= int(input("\n Enter per cost of serving "+breed_name+":\n"))
            p=Pen(breed_name,capacity,cost_per_serving)
            self.farm.createPen(breed_name,p)
            i+=1

    def addCow(self):
        print(self.farm.breed_pen.keys())
        breed_name=input("\n Enter breed name:\n")
        count = int(input("\n Enter number of cows: \n"))

        if self.farm.checkBreed(breed_name):
            breedPen=self.farm.getPen(breed_name)
            if not breedPen.addCows(breed_name,count):
                print("Cannot add. Remaining capacity ="+ str(breedPen.getRemainingCapacity()))
            else:
                print("Successfully added "+breed_name)
        else:
            print(breed_name+" breed doesn't exist in the farm")
        return

    def getMilkEstimate(self):
        print(self.farm.breed_pen.keys())
        breed_name=input("\n Enter breed name: \n")
        days=input("\n How many days of estimate? \n")
        if self.farm.checkBreed(breed_name):
            breedPen=self.farm.getPen(breed_name)
            print(str(breed_name + " pen will generate "+ str(breedPen.getMilk(int(days))) + " gallon of milk in "+ days + " days " ))
        else:
            print(breed_name+" breed doesn't exist in the farm")
        return

    def getCostPen(self):
        print(self.farm.breed_pen.keys())
        breed_name=input("\n Enter breed name : \n")
        days=input(" \n How many days of estimate? \n")
        if self.farm.checkBreed(breed_name):
            breedPen=self.farm.getPen(breed_name)
            print("Cost for feeding pen "+breed_name+" in "+days+" days is "+str(breedPen.getCost(int(days)))+"USD")
        else:
            print(breed_name+" breed doesn't exist in the farm")
        return

    def getCostAllPens(self):
        days=input("\n  How many days of estimate? \n")
        total=0
        for breed,pen in self.farm.breed_pen.items():
            cost=pen.getCost(int(days))
            total+=cost
        print("Total cost of running the farm for  "+days+" = "+str(total)+"USD")
        return


def main():
    farm = Farm()
    rufaas=Main(farm)
    user_input ="y"

    while True:
        if user_input.lower()=="y":
            command=input("\n Enter: \n 1 -> Create Pen \n 2 -> Add cow to pen \n 3 -> Get estimated milk of pen \n 4 -> Get estimated cost of pen(USD) \n 5 -> Get overall estimation(USD)\n")
            if command == "1":
                rufaas.createPen()
            elif command == "2":
                rufaas.addCow()
            elif command == "3":
                rufaas.getMilkEstimate()
            elif command == "4":
                rufaas.getCostPen()
            elif command == "5":
                rufaas.getCostAllPens()
            
            

        else:
            break

        user_input =input("\n Want to continue? (y/n)\n")

        
    
    



main()