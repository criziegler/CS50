def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    contains_special_char = any(
        char in s
        for char in "/,-._"
    )

    starts_with_two_letters = (
        len(s) >= 2 and s[:2].isalpha()
    )
     

    if starts_with_two_letters:
        if len(s) > 6 or contains_special_char or s.startswith("0",2,5):
            return False
        else:
            return True

    else:
        return False
        


main()