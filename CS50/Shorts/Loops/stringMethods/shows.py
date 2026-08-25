SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " spongbob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(", ".join(cleaned_shows))
#    print(cleaned_shows)
#        print(show.strip())
#        print(show.capitalize())
#        print(show.strip().title())


main()

