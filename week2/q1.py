n = int(input(""))
if n <= 0:
    print("輸入錯誤")
num = 1
max = len(str(n * (n + 1) // 2))
for i in range(n):
    for j in range(i+1):
        print(" " * (max - len(str(num))), end="")
        print(str(num)+" ",end='') 
        num+=1
    print("\n",end='')

