from PIL import Image
import numpy as np

im = Image.open("images1/boxes.png")

print(im.format,im.size,im.mode)


# pixelGrid = np.array(im.getdata())

# print()

# pixelGrid=pixelGrid.reshape((im.size[1],im.size[0],len(im.mode)))


# print(pixelGrid)

# # manipulate pixels here


# # convert to image

# pixelGrid = pixelGrid.reshape(im.size[0]*im.size[1],len(im.mode))

# newIm = Image.fromarray(pixelGrid,mode="RGBA")

# newIm.show()


