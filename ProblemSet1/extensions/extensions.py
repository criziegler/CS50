ImageInput = input("File name: ")

def main():
    if ImageInput.endswith(".gif"):
        print("image/gif")
    
    elif ImageInput.endswith(".jpg") or ImageInput.endswith(".jpeg"):
        print("image/jpeg")

    elif ImageInput.endswith(".png"):
        print("image/png")

    elif ImageInput.endswith(".pdf"):
        print("application/pdf")

    elif ImageInput.endswith(".txt"):
        print("text/plain")

    elif ImageInput.endswith(".zip"):
        print("application/zip")

    else:
        print("application/octet-stream")
    
main()