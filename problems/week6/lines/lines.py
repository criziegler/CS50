import sys

loc = []

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")

else:
    if sys.argv[1].endswith(".py"):
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            for line in lines:
                f = line.split("\n")
                loc.append(f)
        
        print(loc)

    else:
        sys.exit("Not a Python file")