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
            starts_with_month = (date_input.startswith(tuple(months)))

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
                    
            elif starts_with_month:
                a, b, c = date_input.split(" ")
                b_formatted = b.strip(",")
                print(b_formatted)
                b_formatted = int(b_formatted)
                
                if a in months_with_30_days_string and b_formatted > 30:
                    pass
                elif a == "February" and b_formatted > 29:
                    pass
                else:
                    print("good")
            
            else:
                pass 

        except KeyboardInterrupt:
            print("\n")
            return

        except KeyError:
            pass

main()