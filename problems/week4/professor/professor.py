import random

def main():

    try:
         
        m = get_level()
        score = 0
        x0 = generate_integer(m)
        y0 = generate_integer(m)

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

def get_level():

    while True:
            n = input("Level: ")
            n = int(n)

            if n == 1 or n == 2 or n == 3:
                return n

            else:
                return n

def generate_integer(level):

        if level == 1:
            level = random.choice(range(0, 9, 1))
            return int(level)

        elif level == 2:
            level = random.choice(range(10, 99, 1))
            return int(level)
        
        elif level == 3:
            level = random.choice(range(100, 99, 1))
            return int(level)
        
        else:
            raise ValueError

if __name__ == "__main__":
    main()  