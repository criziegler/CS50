def main():
#    print_column(3)
#    print_row(4)
    print_square(3)

#def print_column(height):
#    for _ in range(height):
#        print("#")
#    print("#\n" * height, end="")

#def print_row(width):
#    print("?" * width)

def print_square(size):
    #for each row in square
    for i in range(size):
        print_row(size)
#        print("#" * size)
        #for each brick in row
#        for j in range(size):
            #Print brick
#            print("#", end="")

#        print()

def print_row(width):
    print("#" * width)

main()