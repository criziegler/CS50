

def main():

    UserInput = input("")

    if UserInput == "hello :)" or UserInput == "Hello :)":
        print("Hello 🙂")

    elif UserInput == "goodbye :(" or UserInput == "Goodbye :(":
        print("Goodbye 🙁")

    elif UserInput == "Hello :) Goodbye :(" or UserInput == "hello :) goodbye :(":
        print("Hello 🙂 Goodbye 🙁")

    else:
        return

main()