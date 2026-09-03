def main():

    grocery = []

    while True:
        try:
            item = input()
            grocery.insert(0, item)

        except KeyboardInterrupt:
            print(grocery)
            return

        except EOFError:
            print(grocery)
            return
    


main()