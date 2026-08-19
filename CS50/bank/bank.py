UserInput = input("Greeting: ")

def main():
    match UserInput:
        case "Hello" | "hello": 
            print("$0")
        case "h" | "H":
            print("$20")
        case _:
            print("$100")



main()