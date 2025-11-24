n = int(input())
for i in range(n):
    seq = list(input().strip())
    cnt = {}
    for i in seq:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    print(max(cnt, key=cnt.get))