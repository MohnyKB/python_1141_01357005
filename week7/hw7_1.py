def SUM(arr, L, R):
    sub = arr[L : R+1]
    print(sum(sub))

def MAX(arr, L, R):
    sub = arr[L : R+1]
    print(max(sub))

def MIN(arr, L, R):
    sub = arr[L : R+1]
    print(min(sub))

#main()
N = int(input())
arr = [int(x) for x in input().split(" ")]
Q = int(input())
for i in range(Q):
    inst = input().split(" ")
    if len(inst) != 3:
        continue
    op = inst[0]
    i, j = int(inst[1])-1, int(inst[2])-1
    if op == "SUM":
        SUM(arr, i, j)
    elif op == "MAX":
        MAX(arr, i, j)
    elif op == "MIN":
        MIN(arr, i ,j)
#