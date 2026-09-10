import sys
import random
from pyfiglet import Figlet


def main():

    figlet = Figlet()

    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if len(sys.argv) < 2:
            sys.exit("Invalid usage")

        figlet.getFonts()
        fonts = sys.argv[2:4]
        font = fonts[0]
        print(font)
        figlet.setFont(font=font)
        text = input("Input: ")
        output = figlet.renderText(text)
        print("Output: ", output)




main()
