import random

def main():

    user_input = get_level("Level: ")


def get_level(prompt):

    while True:
        try:
            n = input(prompt)
            n = int(n)
            score = 0
            x0 = generate_integer(n)
            y0 = generate_integer(n)

            if n == 1 or n == 2 or n == 3:
                attempts0 = 0

                while attempts0 < 3:
                    math0 = input(f"{x0} + {y0} = ")
                    math0 = int(math0)
                    result0 = x0 + y0

                    if result0 == math0:
                        score = score + 1
                        print("Score:", score)
                        break

                    elif result0 != math0:
                            attempts0 = attempts0 + 1
                            print("EEE")
                            pass    
                    
                if attempts0 == 3:
                    print(f"{x0} + {y0} =", result0)

        except KeyboardInterrupt:
            return

        except EOFError:
            return

def generate_integer(level):

        if level == 1:
            level = random.choice(range(0, 10, 1))
            return int(level)

        elif level == 2:
            level = random.choice(range(0, 20, 1))
            return int(level)
        
        elif level == 3:
            level = random.choice(range(0, 30, 1))
            return int(level)
        
        else:
            raise ValueError

if __name__ == "__main__":
    main()  