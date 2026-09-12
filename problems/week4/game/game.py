import random

def main():

    while True:

        try:
            level = input("Level: ")
            level = int(level)

            if level > 0:
                n = random.choice(range(0, level, 1))

                while True:

                    guess = input("Guess: ")
                    guess = int(guess)

                    try:
                        if guess > 0:
                            if guess == n:
                                print("Just right!")
                                return

                            elif guess > n:
                                print("Too large!")
                                pass

                            elif guess < n:
                                print("Too small!")
                                pass
                        else:
                            pass

                    except KeyboardInterrupt:
                        return
                
                    except EOFError:
                        return
            else:
                pass

        except KeyboardInterrupt:
            return

        except EOFError:
            return

        except ValueError:
            pass                      
            

main()