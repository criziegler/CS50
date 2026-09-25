from PIL import Image

img = Image.new("RGB", (600,600), color="white")
img.save("after.jpg")
quit()