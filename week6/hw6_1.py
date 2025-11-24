class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display(self):
        pass
    
class Car(Vehicle):
    def __init__(self, brand, year, seat):
        super().__init__(brand, year)
        self.seat = seat
    def display(self):
        print(f"Car: {self.brand}, Year: {self.year}, Seat: {self.seat}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = cc
    def display(self):
        print(f"Motorcycle: {self.brand}, Year: {self.year}, cc: {self.cc}")

class Bicycle(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    def display(self):
        print(f"Bicycle: {self.brand}, Year: {self.year}, Model: {self.model}")

#main
vehicles = []


while(True):
    arr = list(input().split())
    if not arr:
        continue
    
    if(arr[0] == "Car"):
        if(len(arr) == 4):
            vehicles.append(Car(arr[1], int(arr[2]), int(arr[3])))
    elif(arr[0] == "Motorcycle"):
        if(len(arr) == 4):
            vehicles.append(Motorcycle(arr[1], int(arr[2]), int(arr[3])))
    elif(arr[0] == "Bicycle"):
        if(len(arr) == 4):
            vehicles.append(Bicycle(arr[1],int(arr[2]), arr[3]))
    elif(arr[0] == "print"):
        for v in vehicles: 
            v.display()
    elif(arr[0] == "stop"):
        break
#