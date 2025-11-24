reflect = {
    'A' : 'A',
    'E' : '3',
    'H' : 'H',
    'I' : 'I',
    'J' : 'L',
    'L' : 'J',
    'M' : 'M',
    'O' : 'O',
    'S' : '2',
    'T' : 'T',
    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X',
    'Y' : 'Y',
    'Z' : '5',
    '1' : '1',
    '2' : 'S',
    '3' : 'E',
    '5' : 'Z',
    '8' : '8',
    '0' : '0'
}

def isPalin(s:str) -> bool:
    i = 0
    j = int(len(s) - 1)
    while(i<=j):
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

def isMirror(s:str) -> bool:
    i = 0
    j = int(len(s) - 1)
    while(i<=j):
        if s[j] not in reflect:
           return False
        if(s[i] != reflect[s[j]]):
            return False
        i += 1
        j -= 1
    return True
    

try:
    while True:
        uwu = input().strip()
        if(isPalin(uwu) and isMirror(uwu)):
            print(f"{uwu} -- is a mirrored palindrome.")
        elif(isMirror(uwu)):
            print(f"{uwu} -- is a mirrored string.")
        elif(isPalin(uwu)):
            print(f"{uwu} -- is a regular palindrome.")
        else:
            print(f"{uwu} -- is not a palindrome.")
except EOFError:
    pass