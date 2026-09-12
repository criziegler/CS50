def main():

    namelist = [ 
        "Liesl",
        "Friedrich",
        "Louisa",
        "Kurt",
        "Brigitta",
        "Marta",
        "Gretl",
    ]

    nameinput = []

    while True:

        try:
            names = input("Name: ")

            if names in namelist:
                nameinput.append(names)
                print(nameinput)


        except KeyboardInterrupt:
            ...


main()