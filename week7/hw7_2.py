def solve():
    s = input().strip()
    
    num_stack = []
    str_stack = []
    
    current_string = ""
    current_num = 0
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
            
        elif char == '(':
            num_stack.append(current_num)
            str_stack.append(current_string)
            
            current_string = ""
            current_num = 0
            
        elif char == ')':
            k = num_stack.pop()
            prev_string = str_stack.pop()
            current_string = prev_string + (current_string * k)
            
        else:
            current_string += char
    print(current_string)

try:
    solve()
except EOFError:
    pass