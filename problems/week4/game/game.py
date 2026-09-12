import random

def main():

    while True:
        try:

            level = input("Level: ")
            level = int(level)

            if level > 0:
                n = random.choice(range(0, level, 1))
                guess = input("Guess: ")
                guess = int(guess)
                print(n)

                if guess == n:
                    print("Yes")
                    return

                else:
                    print("Wrong")
                    pass

        except KeyboardInterrupt:
            return

        except EOFError:
            return

            

main()