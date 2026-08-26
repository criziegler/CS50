def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):


    starts_with_two_letters = (len(s) >= 2 and s[:2].isalpha())

    formatted_plate = (s.endswith() or s.isalpha())

    contains_special_char = any(
        char in s
        for char in "/,-._"
    )

    if starts_with_two_letters and formatted_plate:
        if len(s) > 6 or contains_special_char or s.startswith("0", 2, 6):
            return False
        elif len(s) > 6 or contains_special_char or s.startswith("0", 3, 6) and s[:3].isalpha():
            return False

        elif len(s) > 6 or contains_special_char or s.startswith("0", 4, 6) and s[:4].isalpha():
            return False

        elif len(s) > 6 or contains_special_char or s.startswith("0", 5, 6) and s[:5].isalpha():
            return False
        
        else:
            return True
           
    else:
        return False


        


main()