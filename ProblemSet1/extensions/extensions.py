ImageInput = input("File name: ")

def main():
    if ImageInput.endswith(".gif"):
        print("Image/gif")
    
    elif ImageInput.endswith(".jpg") or ImageInput.endswith(".jpeg"):
        print("Image/jpeg")

    elif ImageInput.endswith(".png"):
        print("Image/png")

    elif ImageInput.endswith(".pdf"):
        print("application/pdf")

    elif ImageInput.endswith(".txt"):
        print("text/plain")

    elif ImageInput.endswith(".zip"):
        print("application/zip")

    else:
        print("application/octet-stream")
    
main()