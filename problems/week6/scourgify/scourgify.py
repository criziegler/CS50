import sys
import csv

from tabulate import tabulate


if len(sys.argv) == 1 or len(sys.argv) == 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 4:
    sys.exit("Too many command-line arguments")

else:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            students = list(csv.DictReader(file))


        with open(sys.argv[2], "w") as f:

            writer = csv.DictWriter(f, fieldnames=["name","house"])
            writer.writeheader()

            for student in sorted(students, key=lambda student: student["name"].split(",")[1]):
                last_name, first_name = student["name"].split(",", 1)
                f_name = f"{first_name}, {last_name}"

                formatted_dict = {"name": f_name, "house": student["house"]}
                writer.writerow(formatted_dict)



    else:
        sys.exit("Not a CSV file")