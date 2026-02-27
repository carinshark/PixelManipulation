from PIL import Image
import numpy as np



class Pixelgrid:


    def __init__(self,image_link:str):
        self.image = Image.open(image_link)

        self.filetype =image_link[image_link.index("."):]
        
        self.grid = np.array(self.image)
        self.columns=self.image.size[0]
        self.rows = self.image.size[1]
        self.grid=self.grid.reshape((self.rows,self.columns,len(self.image.mode)))
    
    def newImage(self):
        self.image = Image.fromarray(self.grid,mode=self.image.mode)

    def show(self):
        self.newImage()

        self.image.show()
    
    
    def save(self,filename):
        self.newImage()

        self.image.save(filename)
    

    