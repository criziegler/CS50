def main():

    fuel = convert(input("Fraction: "))

    print(fuel)

def convert(fraction):


    x,y = fraction.split(sep="/")
    x = int(x)
    y = int(y)

    if x >= 0 and y >= 0 and x / y <= 1:
        result = x / y * 100
        return gauge(int(result))
         
    elif x > y:
        raise ValueError

    elif y == 0:
        raise ZeroDivisionError

    else: 
        raise ValueError

def gauge(percentage):

    z = int(percentage)

    if z <= 1:
        return "E"
    
    elif z >= 99:
        return "F"

    else:
        return f"{z}%" 


if __name__ == "__main__":
    main()