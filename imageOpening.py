from PIL import Image
import numpy as np

im = Image.open("images1/green.jpg")

print(im.format,im.size,im.mode)


pixelGrid = np.array(im)

print()

pixelGrid=pixelGrid.reshape((im.size[1],im.size[0],len(im.mode)))



# manipulate pixels here

print(pixelGrid.shape)

for row in range(pixelGrid.shape[0]):
    break
    for column in range(pixelGrid.shape[1]):
        pixel = pixelGrid[row,column]
        r,g,b= tuple(pixel)

        r=0

        
        


        pixelGrid[row,column] = np.array((r,g,b))


newGrid = pixelGrid.copy()

    
for row in range(pixelGrid.shape[0]//2):
        
        if row%2==0:
            print(row,pixelGrid.shape[0]-row-1)
            
            newGrid[row] = pixelGrid[pixelGrid.shape[0]-row-1]
            newGrid[pixelGrid.shape[0]-row-1] = pixelGrid[row]

            
pixelGrid=newGrid

# for row in range(pixelGrid.shape[0]):
#      np.random.shuffle(pixelGrid[row])

# np.random.shuffle(pixelGrid)

    
    

# convert to image


newIm = Image.fromarray(pixelGrid,mode=im.mode)

newIm.show()


