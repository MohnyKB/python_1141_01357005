import math

def ans(N):
    G = int()
    for i in range(1,N):
        for j in range(i+1,N+1):
            G += math.gcd(i,j)
    return G

#main
temp = int(input())
while(temp != 0):
    print((ans(temp)))
    temp = int(input())
#