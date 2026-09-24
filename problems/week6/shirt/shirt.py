import sys
import csv
from PIL import Image

from tabulate import tabulate

try:

    if len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 4:
        sys.exit("Too many command-line arguments")

    else:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            with open(sys.argv[1], "r") as file:
               ... 


        else:
            sys.exit("Input and output have different extensions")

except FileNotFoundError:
    sys.exit("Input does not exist")