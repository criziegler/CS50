import sys
import random
from pyfiglet import Figlet


def main():

    figlet = Figlet()

    if len(sys.argv) < 2:
        sys.exit("Invalid usage")

    elif sys.argv[1] == "-f":
        if len(sys.argv) < 4:
            sys.exit("Invalid usage")

        font = sys.argv[2]

  
main()
