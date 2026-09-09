def main():
    user_input = split_at_uppercase(input("camelCase: "))
    print("snake_case: ",user_input)
    
        
def split_at_uppercase(word):
    result = ""
    for char in word:
        if char.isupper() and result:
            result += "_"
        result += char
    formatted_result = result.lower()
    return formatted_result





main()