
class bank():

    def __init__(self):
        self.dict = {}

    def deposit(self, name, val):
        if(name not in self.dict):
            print("Account not found")
        else:
            self.dict[name] += val

    def withdraw(self, name, val):
        if(name not in self.dict):
            print("Account not found")
        elif (self.dict[name] < val):
            print("Insufficient funds")
        else:
            self.dict[name] -= val

    def balance(self, name):
        if(name not in self.dict):
            print("Account not found")
        else:
            print(self.dict[name])
    
    def create(self, name, val):
        self.dict[name] = val

##main
myBank = bank()
while True:

    line = input()

    if not line:
        continue

    if line == "stop":
        break

    parts = line.split()
    ops = parts[0]

    if ops == "stop":
        break

    obj = parts[1]

    if ops == "create" :
        val = int(parts[2])
        myBank.create(obj, val)

    elif ops == "deposit":
        val = int(parts[2])
        myBank.deposit(obj, val)

    elif ops == "withdraw":
        val = int(parts[2])
        myBank.withdraw(obj, val)

    elif ops == "balance":
        myBank.balance(obj)
##