def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:

        try:
            date_input = input("Date: ")
            start_with_digit = (date_input[:1].isdigit())

            if start_with_digit:
                x, y, z = date_input.split("/")
                print(f"{z}-{x}-{y}")
                return

            elif date_input.startswith(tuple(months)):
                print("yes")
            
            else:
                pass 

        except KeyboardInterrupt:
            print("\n")
            return

        except KeyError:
            pass

main()