import sys
import csv

from tabulate import tabulate

try:

    if len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 4:
        sys.exit("Too many command-line arguments")

    else:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            with open(sys.argv[1], "r") as file:
                students = list(csv.DictReader(file))

            with open(sys.argv[2], "w") as after:

                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"], lineterminator="\n")
                writer.writeheader()

                for student in students:
                    last, first = student["name"].split(",", 1)

                    writer.writerow({
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": student["house"]
                    })


        else:
            sys.exit("Not a CSV file")

except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")