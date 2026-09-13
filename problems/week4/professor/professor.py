import random

def main():

    while True:
        lev = get_level("Level: ")


def get_level(prompt):

    level_list = [1, 2, 3]

    while True:
        try:
            n = input(prompt)
            n = int(n)

            if n in level_list:
                print("yes")
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