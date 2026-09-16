def main():

    greetings = value(input("Greeting: "))
    print(greetings)

def value(greeting):

    if greeting.startswith("Hello") or greeting.startswith("hello"):
        return "$0"
    
    elif greeting.startswith("h") or greeting.startswith("H"):
        return "$20"
    
    else:
        return "$100"



if __name__ == "__main__":
    main()