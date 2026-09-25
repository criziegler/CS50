import sys
from PIL import Image

try:

    if len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 4:
        sys.exit("Too many command-line arguments")

    else:

        image1 = sys.argv[1].lower()
        image2 = sys.argv[2].lower()

        if (image1.endswith(".jpg") and image2.endswith(".jpg") 
            or image1.endswith(".jpeg") and image2.endswith(".jpeg") 
            or image1.endswith(".png") and image2.endswith(".png")):

            shirt = Image.open("shirt.png")

            size = (0,100,600,700)
            
            image = Image.open(sys.argv[1])
            image_re = image.resize((600,800))
            image_new = image_re.crop(size)

            after = Image.open(sys.argv[2])
            after.paste(image_new)
            after.paste(shirt, shirt)
            after.save(sys.argv[2])

        else:
            sys.exit("Input and output have different extensions")

except FileNotFoundError:
    sys.exit("Input does not exist")