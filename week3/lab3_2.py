n = int(input())
while True:
    seq = list(map(int, input().split()))
    if seq[0] == 0:
        break

    stack = []
    current = 1
    possible = True

    for target in seq:
        while current <= n and (not stack or stack[-1] != target):
            stack.append(current)
            current+=1
        if stack and stack[-1] == target:
            stack.pop()
        else:
            possible=False
            break
    print("YES" if possible else "NO")