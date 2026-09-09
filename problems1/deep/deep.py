UserInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

def main():  
    if UserInput == "42":
        print("Yes")

    elif UserInput == "forty-two" or UserInput == "Forty-Two":
        print("Yes")

    elif UserInput == "forty two" or UserInput == "Forty Two":
        print("Yes")

    else:
        print("No")
    
    return

main()

