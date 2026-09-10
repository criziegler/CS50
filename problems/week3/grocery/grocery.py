def main():

    grocery = []

    while True:

        try:
            items = input()
            grocery.append(items)
            upper_list = [item.upper() for item in grocery]
            upper_list.sort() 

            counts = {word: items.count(word) for word in upper_list}

            for word in upper_list:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

        except KeyboardInterrupt:
            print("\n")
            if grocery == []:
                return
            else:
                for key,value in counts.items():
                    print(f"{value} {key}")
                return       

        except EOFError:
            print("\n")
            if grocery == []:
                return
            else:
                for key,value in counts.items():
                    print(f"{value} {key}")
                return
        

main()