def main():

    grocery = []
    lower_list = []
    upper_list = []

    while True:
        try:
            item = input()
            grocery.append(item)

        except KeyboardInterrupt:
            print(grocery)
            return

        except EOFError:
            print(grocery)
            return
    


main()