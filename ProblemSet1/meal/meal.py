
def main():
    currentTime = convert(input("What time is it? "))


    if currentTime >= 7.0 and currentTime <= 8.0:
        print("breakfast time")

    elif currentTime >= 12.0 and currentTime <= 13.0:
        print("lunch time")

    elif currentTime >= 18.0 and currentTime <= 19.0:
        print("dinner time")

    else:
        return

def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)
    decimal_hours = hours + minutes / 60

    return(decimal_hours)


if __name__ == "__main__":
    main()
