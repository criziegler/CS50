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

    months_with_30_days = [4, 6, 9, 11]

    months_with_30_days_string = ["April", "June", "September", "November"]

    while True:

        try:
            date_input = input("Date: ")
            start_with_digit = (date_input[:1].isdigit())
            # months_with_30_days = [4, 6, 9, 11]

            if start_with_digit:
                x, y, z = date_input.split("/")
                x = int(x)
                y = int(y)
                if x <= 12 and y <= 31:
                    if x in months_with_30_days and y > 30:
                        pass
                    elif x == 2 and y > 29:
                        pass
                    else:    
                        if x <= 9 and y >= 10:
                            print(f"{z}-0{x}-{y}")
                            return
                        elif y <= 9 and x >= 10:
                            print(f"{z}-{x}-0{y}")
                            return
                        elif x <= 9 and y <= 9:
                            print(f"{z}-0{x}-0{y}")
                            return
                        else:
                            print(f"{z}-{x}-{y}")
                            return
                else:
                    pass
                    
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