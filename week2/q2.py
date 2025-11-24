n = int(input(""))
arr = list(map(int, input("").split(" ")))
print("排序前的數列: ",end="")
for i in arr:
    print(str(i)+' ',end="")
print()
arr.sort() 
print("排序後的數列: ",end="")
for i in arr:
    print(str(i)+' ',end="")