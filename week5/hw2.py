arr = []
n = 0

try:
    n = int(input())  
    for i in range(n):
        try:
            raw = input()
            temp = raw.split(',')
            if len(temp) != 2 or not temp[0] or not temp[1]:
                print("Error: invalid data format")
                continue
            name, score_str = temp[0],temp[1]
            score = int(score_str)
            
            if not (0 <= score <= 100):
                raise ValueError

            print("OK")
            arr.append(score)
            
        except ValueError:
            print("Error: invalid score")
            continue
            
        except EOFError:
            break 

finally:
    if len(arr) == 0:
        print("No valid scores")
    else:
        average = sum(arr) / len(arr)
        print(f"Average score: {average:.2f}")