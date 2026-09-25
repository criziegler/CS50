import sys
from PIL import Image

try:

    if len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 4:
        sys.exit("Too many command-line arguments")

    else:
        if sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg"):
            shirt = Image.open("shirt.png")

            shirt_re = shirt.resize((1200,1600))

            size = (0,200,1200,1500)
            
            image = Image.open(sys.argv[1])
            image_re = image.crop(size)

            after = Image.open(sys.argv[2])
            after_re = after.crop(size)
            after_re.paste(image_re)
            after_re.paste(shirt_re, (0,-300), shirt_re)

            after_re.save(sys.argv[2])

        else:
            sys.exit("Input and output have different extensions")

except FileNotFoundError:
    sys.exit("Input does not exist")