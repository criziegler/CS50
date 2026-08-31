def area(length, width):
    print(str(length * width) + " m2")
    return length * width


def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + " total m2")

main()

