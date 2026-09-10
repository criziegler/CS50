def main():

    print("Amount Due: 50")
    amount_due = 50

    while True:
        n = int(input("Insert Coin: "))

        if n == 25 or n == 10 or n == 5:
            amount_due -= n

            if amount_due <= 0:
                print("Change Owed:",abs(amount_due))

                break

            else: 

                print("Amount Due:",amount_due)

        else:
            print("Amount Due:",amount_due)
        
main()