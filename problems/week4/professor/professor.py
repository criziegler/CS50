import random

def main():

    user_input = get_level("Level: ")


def get_level(prompt):

    while True:
        try:
            n = input(prompt)
            n = int(n)

            if n == 1 or n == 2 or n == 3:
                x0 = generate_integer(n)
                y0 = generate_integer(n)
                math0 = input(f"{x0} + {y0} = ")
                result0 = x0 + y0

                while True:
                    if result0 == math0:
                        print("yes")
                        break
                    elif result0 != math0:
                        for i in range(3):
                            print("EEE")
                        print(result0)

                    else:
                        break
            
            else:
                pass

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