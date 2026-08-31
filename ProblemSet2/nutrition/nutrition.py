fruitsdict = {
            "Apple": "130", 
            "Avocado": "50",
            "Banana": "110",
            "Cantaloupe": "50",
            "Grapefruit": "60",
            "Grapes": "90",
            "Honeydew Melon": "50",
            "Kiwifruit": "90",
            "Lemon": "15",
            "Lime": "20",
            "Nectarine": "60",
            "Orange": "80",
            "Peach": "60",
            "Pear": "100",
            "Pineapple": "50",
            "Plums": "70",
            "Strawberries": "50",
            "Sweet Cherries": "100",
            "Tangerline": "50",
            "Watermelon": "80"
            }

def main():

    formatted_list = set(key.lower() for key in fruitsdict)

    user_input = input("Item: ")

    while True:
        if user_input in fruitsdict:
            print("Calories:",fruitsdict[user_input])
            break

        elif user_input in formatted_list:
            user_input.capitalize()
            print("Calories:",fruitsdict[user_input.capitalize()])
            break

        else: 
            break

main()