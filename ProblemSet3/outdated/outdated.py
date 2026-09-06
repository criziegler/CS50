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

    months_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    months_with_30_days = [4, 6, 9, 11]

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

            elif date_input.startswith(" ") and date_input.endswith(" "):
                date_input.strip()
                d, e, f = date_input.split("/")
                d = int(d)
                e = int(e)
                f = f.strip()
                if d <= 12 and e <= 31:
                    if d <= 9 and e <= 9:
                        print(f"{f}-0{d}-0{e}")
                        return
                    elif d <= 9 and e >= 10:
                        print(f"{f}-0{d}-{e}")
                        return
                    elif d >= 10 and e <= 9:
                        print(f"{f}-{d}-0{e}")
                        return
                    else:
                        print(f"{f}-{d}-{e}")
                        return

                else:
                    pass        
                    
            elif starts_with_month and date_input.index(","):
                a, b, c = date_input.split(" ")
                b_formatted = b.strip(",")
                b_formatted = int(b_formatted)

                if starts_with_month and b_formatted <= 31:
                    if any(months[i] == a for i in months_with_30_days) and b_formatted > 30:
                        pass
                    elif a == "February" and b_formatted > 29:
                        pass
                    else:
                        months_dict = dict(zip(months, months_value))

                        if a in months[:9] and b_formatted >= 10:
                            print(f"{c}-0{months_dict[a]}-{b_formatted}")
                            return
                        elif a in months[9:12] and b_formatted <= 9 :
                            print(f"{c}-{months_dict[a]}-0{b_formatted}")
                            return
                        elif a in months[:9] and b_formatted <= 9:
                            print(f"{c}-0{months_dict[a]}-0{b_formatted}")
                            return
                        else:
                            print(f"{c}-{months_dict[a]}-{b_formatted}")
                            return
                
            else:
                return 

        except ValueError:
            ...
        
        except KeyboardInterrupt:
            print("\n")
            return


main()