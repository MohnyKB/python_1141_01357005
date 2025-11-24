def nextGen(patt):
    next = [0 for i in patt]
    length = 0
    for i in range(1, len(patt)):
        while patt[i] != patt[length] and length > 0:
            length = next[length-1]
        if patt[i] == patt[length]:
            length += 1
        next[i] = length

    return next

def kmp(txt, patt):
    if len(patt) == 0:
        return []
    
    next = nextGen(patt)
    j = 0
    ans = []

    for i in range(len(txt)):
        while j > 0 and txt[i] != patt[j]:
            j = next[j-1]
        if txt[i] == patt[j]:
            j+=1
        if j == len(patt):
            ans.append(i - j + 1)
            j = next[j-1]
    return ans
        
##main
txt = input().strip()
patt = input().strip()
ans = kmp(txt, patt)
for i in ans:
    print(f"{i} ", end="")
##