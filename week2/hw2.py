arr = []
while True:
    try:
        x = int(input(""))
        arr.append(x)
        arr.sort()
        if(len(arr)%2 == 1):
            print(arr[len(arr)//2])
        else:
             print((arr[len(arr)//2 - 1] + arr[len(arr)//2]) // 2)
    except EOFError:
        break
