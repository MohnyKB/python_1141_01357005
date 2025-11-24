import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left = []
        right = []
        mid = []
        p = random.choice(arr)

        for i in arr:
            if i < p:
                left.append(i)
            if i > p:
                right.append(i)
            if i == p:
                mid.append(i)
    
        Sleft = quicksort(left)
        Sright = quicksort(right)

        return Sleft + mid + Sright
          

##main
arr = input().split(' ')
iarr = [int(i) for i in arr]
Sarr = quicksort(iarr)
print(*Sarr)
##