from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():


    user_input = input("Input: ")


    print(figlet.renderText(user_input))



    # f = pyfiglet.figlet_format("text to render",font="slant")
    # print(f)


main()
