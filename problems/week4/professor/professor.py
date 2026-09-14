import random

def main():

    try:
 
        m = get_level()
        score = 0
        attempts = 0

        for xy in range(10):
            x = generate_integer(m)
            y = generate_integer(m)

            for attempts in range(3):
                user_input = input(f"{x} + {y} = ")
                result = x + y

                if int(user_input) == x + y:
                    score = score + 1
                    break

                else:
                    print("EEE")
                    if attempts == 2:
                        print(f"{x} + {y} = {result}")

                attempts = attempts + 1

        print("Score:", score)
        return

    except KeyboardInterrupt:
        return

    except EOFError:
        return

def get_level():

    while True:
        try:
            n = input("Level: ")
            n = int(n)

            if n == 1 or n == 2 or n == 3:
                return n

            else:
                pass

        except ValueError:
            pass

def generate_integer(level):

        if level == 1:
            level = random.randint(0, 9)
            return int(level)

        elif level == 2:
            level = random.randint(10, 99)
            return int(level)
        
        elif level == 3:
            level = random.randint(100, 999)
            return int(level)
        
        else:
            raise ValueError

if __name__ == "__main__":
    main()  