from PIL import Image
import numpy as np

im = Image.open("images1/ship.png")

print(im.format,im.size,im.mode)


pixelGrid = np.array(im)

print()

pixelGrid=pixelGrid.reshape((im.size[1],im.size[0],4))



# manipulate pixels here

print(pixelGrid.shape)

for row in range(pixelGrid.shape[0]):
    for column in range(pixelGrid.shape[1]):
        pixel = pixelGrid[row,column]
        r,g,b,a= tuple(pixel)

        r,g,b= g,b,r


        pixelGrid[row,column] = np.array((r,g,b,a))
    
    
    

# convert to image


newIm = Image.fromarray(pixelGrid,mode="RGBA")

newIm.show()


