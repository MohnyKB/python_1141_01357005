n = int(input(""))
if(not(n>1)):
    print("輸入錯誤")
else:
    print(" "*(n-1)+"*")
    for i in range(2,n):
        print( " "*(n-i) + "*" + " "*(2*i-3) + "*")
    print("*"*(2*n-1),end="")