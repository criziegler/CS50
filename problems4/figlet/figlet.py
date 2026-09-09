import sys
import random
from pyfiglet import Figlet


def main():

    figlet = Figlet()
    user_input = input("Input: ")

    if sys.argv[2] in figlet.getFonts():
        x, y = sys.argv[2].split(" ")
        print (x,y)
        print(figlet.renderText(user_input))

    elif figlet.setFont(font="slant"):
        print(figlet.renderText(user_input, font="slant"))
    else:
        ...



main()
