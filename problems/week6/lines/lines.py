import sys

loc = []

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")

else:
    if sys.argv[1].endswith(".py"):
        with open(sys.argv[1], "r") as file:

            for lines in file:
                loc.append(lines.strip())

            lines_list = [line for line in loc if line.strip()]
            # filtered_list = list(filter(lambda s: not s.startswith("#"), lines_file))
            count = 0

            for word in lines_list:
                if word.startswith("#"):
                    lines_list.remove(word)
                    count += 1

                else:
                    count += 1
        
        print(count)

    else:
        sys.exit("Not a Python file")