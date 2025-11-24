n1, n2 = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a & b))
print(" ".join(map(str, sorted(a & b))))