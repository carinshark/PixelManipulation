from PIL import Image
import numpy as np


class Pixelgrid:


    def __init__(self,image_link:str):
        self.image = Image.open(image_link)

        
        self.grid = np.array(self.image)
        self.columns=self.image.size[0]
        self.rows = self.image.size[1]
        self.grid=self.grid.reshape((self.rows,self.columns,len(self.image.mode)))
    

    def show(self):
        newIm = Image.fromarray(self.grid,mode=self.image.mode)

        newIm.show()