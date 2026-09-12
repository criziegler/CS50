def main():

    namedict = { 
        "Liesl": "Adieu, adieu, to Liesl",
        "Friedrich": "Adieu, adieu, to Liesl and Friedrich",
        "Louisa": "Adieu, adieu, to Liesl, Friedrich, and Louisa",
        "Kurt": "Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt",
        "Brigitta": "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta",
        "Marta": "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta",
        "Gretl": "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl",
    }

    nameinput = []

    while True:
        try:
            names = input("Name: ")

            if names in namedict:
                nameinput.append(names)

            else:
                return
            
        except KeyboardInterrupt:
            print("\n")
            print(namedict[nameinput[-1]])
            return

        except EOFError:
            print("\n")
            print(namedict[nameinput[-1]])
            return


main()