def cola(cans: int) -> int:
    total = 0
    while cans >= 3:
        new = cans // 3
        total += new
        cans = new + cans % 3
    if cans == 2:
        total += 1
    return total

try:
    while True:
        n = int(input())
        if n == 0:
            break
        print(n + cola(n))
except EOFError:
    pass