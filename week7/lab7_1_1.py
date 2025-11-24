import re
from collections import Counter

def vocFreq(txt):
    lowerTxt = txt.lower()
    words = re.findall(r'[a-z]+', lowerTxt)
    return Counter(words)

def charFreq(txt):
    lowerTxt = txt.lower()
    letters = (char for char in lowerTxt if char.isalpha())
    return Counter(letters)

def getTop(dic):
    arr = list(dic.items())
    arr.sort(key=lambda item: item[1], reverse=True)
    return arr[:3]
