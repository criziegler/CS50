UserInput = input("Greeting: ")

def main():

    if UserInput.startswith("Hello") or UserInput.startswith("hello"):
        print("$0")
    elif UserInput.startswith("h") or UserInput.startswith("H"):
        print("$20")
    else:
        print("$100")


main()