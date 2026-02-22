from PIL import Image

im = Image.open("images1/ship.png")

print(im.format,im.size,im.mode)

im.show()
