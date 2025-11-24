def count_carry_operations(in1: str, in2: str) -> int:
    num1 = [int(digit) for digit in in1]
    num2 = [int(digit) for digit in in2]

    temp = 0
    counter = 0

    for index in range(1, min(len(num1), len(num2)) + 1):
        if num1[-index] + num2[-index] + temp > 9:
            counter += 1
            temp = 1
        else:
            temp = 0

    longer = num1 if len(num1) > len(num2) else num2
    for index in range(min(len(num1), len(num2)) + 1, len(longer) + 1):
        if longer[-index] + temp > 9:
            counter += 1
            temp = 1
        else:
            temp = 0

    return counter

while True:
    in1, in2 = input().split()
    if in1 == "0" and in2 == "0":
        break
    
    temp = count_carry_operations(in1, in2)
    if temp == 0:
        print("No carry operation.")
    elif temp == 1:
        print(f"{temp} carry operation.")
    else:
        print(f"{temp} carry operations.")