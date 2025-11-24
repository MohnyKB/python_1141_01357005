import lab7_1_1
import sys

def main():
    try:
        with open("input.txt", 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        return
    except Exception as e:
        return
    
    wordCount = lab7_1_1.vocFreq(text)
    charCount = lab7_1_1.charFreq(text)

    topWord = lab7_1_1.getTop(wordCount)
    topChar = lab7_1_1.getTop(charCount)

    for word, count in topWord:
        print(f"{word}: {count} ", end="")
    print()

    for letter, count in topChar:
        print(f"{letter}: {count} ", end="")
if __name__ == "__main__":
    main()