def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
#            x = int(input("What's x? "))
        except ValueError:
            pass
#            print("x is not an integer")
#        else:
#            return x


main()
