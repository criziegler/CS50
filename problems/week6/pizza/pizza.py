import sys
import csv

from tabulate import tabulate


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")

else:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:

            table = list(csv.DictReader(file))

            print(tabulate(table, headers = "keys", tablefmt="grid"))

    else:
        sys.exit("Not a CSV file")