
def main():

    input_word = remove_vowels(input("Input: "))

    print("Output:",input_word)

def remove_vowels(word):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    result = ""

    for char in word:
        if char not in vowels:
            result = result + char
        
    return result

main()