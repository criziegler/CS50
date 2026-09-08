import emoji

emojilist = [
    ":1st_place_medal:",
    ":money_bag:",
    ":smile_cat:",
]

def main():

    user_input = input("Input: ")
    try:
        if user_input in emojilist:
            print(emoji.emojize(user_input))
            return
    except:
        pass


main()


