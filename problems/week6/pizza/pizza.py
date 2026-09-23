import sys
import csv

from table2ascii import table2ascii, Alignment, PresetStyle


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")

else:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:

            menu_body = {}
            
            menu = csv.DictReader(file)
            for row in menu:
                ...

            print(menu)

            # menu = table2ascii(
            #     header = menu_header,
            #     body = [menu_body[:]],
            #     style=PresetStyle.ascii_box
            # ) 

            # print(menu)


    else:
        sys.exit("Not a CSV file")