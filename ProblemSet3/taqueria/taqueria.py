menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

def main():
    try:
        order = get_input("Item: ")

    except KeyboardInterrupt:
        print("\n")
        return
    
    except EOFError:
        print("\n")
        return

def get_input(prompt):
    formatted_list = set(key.lower() for key in menu)

    total = 0.00

    while True:
        item = input(prompt)
        try:
            if item in menu:
                total = total + menu[item]
                print(f"Total: ${total:.2f}")

            elif item in formatted_list:
                total = total + menu[item.title()]
                print(f"Total: ${total:.2f}")

        except KeyError:
            pass

main()