import pyfiglet
import sys


def main():

    user_input = input("Input: ")

    if len(sys.argv) == 2:
        print(pyfiglet.figlet_format(user_input, sys.argv[2]))

    else:
        print(pyfiglet.figlet_format(user_input))



    # f = pyfiglet.figlet_format("text to render",font="slant")
    # print(f)


main()
