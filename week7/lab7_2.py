def R(arr):
    if not arr:
        return []
    N = len(arr)

    temp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp[j][N- i - 1] = arr[i][j]
    return temp


def V(arr):
    if not arr:
        return []
    N = len(arr)

    temp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
       for j in range(N):
        temp[i][N - 1 - j] = arr[i][j]

    return temp

def H(arr):
    if not arr:
        return []
    N = len(arr)

    temp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp[N- i - 1][j] = arr[i][j]

    return temp


##main
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = input().split()
    for j in range(N):
        arr[i][j] = int(row[j])

txt = input().strip()
for i in txt:
    if i == "R":
        arr = R(arr)
    elif i == "H":
        arr = H(arr)
    elif i == "V":
        arr = V(arr)
    else:
        emp = 0
for i in arr:
    for j in i:
        print(f"{j} ",end = "")
    print()
##  