from PIL import Image

img = Image.new("RGB", (1200,1600), color="white")
img.save("after.jpg")
quit()