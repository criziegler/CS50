import random

def main():

    lev = get_level("Level: ")


def get_level(prompt):

    while True:
        try:
            n = input(prompt)
            n = int(n)

            if n == 1:
                while True:
                    x = generate_integer(n)
                    y = generate_integer(n)

                    result = x + y

                    user_result = input(f"{x} + {y} = ")

                    if result == user_result:
                        print("yes")
                        break

                    else:
                        break
             
            elif n == 2:
                x = generate_integer(n)
                y = generate_integer(n)
                print(x)
                print(y)
                return
             
            elif n == 3:
                x = generate_integer(n)
                y = generate_integer(n)
                print(x)
                print(y)
                return
            
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