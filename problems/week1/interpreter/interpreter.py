
def main():
    expression = input("Expression: ")
    x, y, z = expression.split()
    x = int(x)
    z = int(z)

    if y == "+":
        print(float(x + z))

    elif y == "-":
        print(float(x - z))

    elif y == "*":
        print(float(x + z))

    elif y == "/" and z != 0:
        print(float(x / z))

    else: 
        print("Syntax error")

main()


