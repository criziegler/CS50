def main ():

    fuel = get_int("Fraction: ")
    print(fuel)

def get_int(prompt):

    while True:
        try:
            n = input(prompt)
            x,y = n.split(sep="/")
            x = int(x)
            y = int(y)

            if x >= 0 and y >= 0 and x / y <= 1:
                if x / y <= 0.01:
                    return("E")
                elif x / y >= 0.99:
                    return("F")
                else:
                    result = x / y * 100
                    result = str(f"{int(result)}%")
                    return result      

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

main()