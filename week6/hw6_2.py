class Matrix:
    def __init__(self):
        self.data = None
        self.size = 0

    def scan(self):
        n = int(input())
        self.size = n
        self.data = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            arr = input().split()
            for j in range(n):
                self.data[i][j] = int(arr[j])

    def RR(self):
        if self.data is None:
            print("No element in matrix can be rotated.")
            return
        else:
            n = self.size
            temp = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    temp[j][n-i-1] = self.data[i][j]
            self.data = temp
    
    def RL(self):
        if self.data is None:
            print("No element in matrix can be rotated.")
            return
        else:
            n = self.size
            temp = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    temp[n-j-1][i] = self.data[i][j]
            self.data = temp
    def print(self):
        if self.data is None:
            print("No element in matrix can be printed.")
            return
        else:
            for row in self.data:
                print(*row)

#main
matrix = Matrix()

while True:
    op = str(input()).strip()
    if not op:
        continue
    if(op == "scan"):
        matrix.scan()
    elif(op == "rotate right"):
        matrix.RR()
    elif(op == "rotate left"):
        matrix.RL()
    elif(op == "print"):
        matrix.print()
    elif(op == "stop"):
        break

#