import random

def main():

    lev = get_level("Level: ")


def get_level(prompt):

    level_list = [1, 2, 3]

    while True:
        try:
            n = input(prompt)
            n = int(n)

            if n == 1:
                print("yes")
                return 1
            elif n == 2:
                print("yes")
                return 2
            elif n == 3:
                print("yes")
                return 3
            else:
                pass

        except KeyboardInterrupt:
            return

        except EOFError:
            return

def generate_integer(level):
    ...


if __name__ == "__main__":
    main()  