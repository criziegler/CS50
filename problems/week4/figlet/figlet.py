import sys
import random
from pyfiglet import Figlet


def main():

    figlet = Figlet()

    try:

        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if len(sys.argv) < 2:
                sys.exit("Invalid usage")

            figlet.getFonts()
            fonts = sys.argv[2:4]
            font = fonts[0]
            figlet.setFont(font=font)
            text = input("Input: ")
            output = figlet.renderText(text)
            print("Output: ", output)

        else:
            sys.exit("Invalid usage")

    except IndexError:
        text_random = input("Input: ")
        font_list = figlet.getFonts()
        font_random = random.choice(font_list)
        figlet.setFont(font=font_random)
        output_random = figlet.renderText(text_random)
        print("Output: ", output_random)



main()
