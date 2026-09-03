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
        get_input("Item: ")

    except KeyboardInterrupt:
        print("\n")
        return
    
    except EOFError:
        print("\n")
        return

# def case_insensetive_input(menu, query):
#     query_normal = query.lower()
#     for key, value in menu.items():
#         if isinstance(key, str) and key.lower() == query_normal:
#             return value
#         return None

def get_input(prompt):
    lower_dict = {key.lower(): value for key, value in menu.items()}
    upper_dict = {k.upper(): v for k, v in menu.items()}

    total = 0.00

    while True:
        item = input(prompt)
        try:
            if item in menu:
                total = total + menu[item]
                print(f"Total: ${total:.2f}")

            elif item in lower_dict:
                total = total + lower_dict[item]
                print(f"Total: ${total:.2f}")

            elif item in upper_dict:
                total = total + upper_dict[item]
                print(f"Total: ${total:.2f}")

        except KeyError:
            pass

main()