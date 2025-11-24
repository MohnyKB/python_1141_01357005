ans = None
count = 0
game_can_start = False

try:
    ans_input = input()
    try:
        ans = int(ans_input)
        if not (0 <= ans <= 50):
            print("Error: number out of range")
        else:
            game_can_start = True
    except ValueError:
        if "." in ans_input:
            print("Error: please enter an integer")
        else:
            print("Error: please enter a number")
    except EOFError:
        pass
    if game_can_start:
        while True:
            try:
                guess_input = input()
                count+=1

                guess = int(guess_input)
                if not (0 <= guess <= 50):
                    print("Error: number out of range")
                    continue
            except ValueError:
                if "." in guess_input:
                    print("Error: please enter an integer")

                else:
                    print("Error: please enter a number")
                continue
            except EOFError:
                break
            else:
                if guess < ans:
                    print("You are too low!")
                elif guess > ans:
                    print("You are too high!")
                else:
                    print("You got it!")
                    break
finally:
    print(f"You guessed {count} times.")