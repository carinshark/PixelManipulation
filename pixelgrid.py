from PIL import Image

import numpy as np
from time import time,sleep
import random

class Pixelgrid:


    def __init__(self,image_link=None,maxSize=200):
        
        if image_link==None:
            image_link=".png"
            self.wasRandom=True
            self.image=Image.fromarray(
                np.array([[[random.randint(0,255) for _ in range(3)
                ] for _ in range(maxSize)] for _ in range(maxSize)],dtype="uint8"))
        else:
            self.image = Image.open(image_link)
            self.wasRandom=False


        if self.image.size[1]>maxSize:
            h=maxSize
            w=int((h/self.image.height)*self.image.width)
            self.image=self.image.resize((w,h),resample=Image.Resampling.NEAREST)
        elif self.image.size[0]>maxSize:
            w=maxSize
            h=int((w/self.image.width)*self.image.height)

            self.image=self.image.resize((w,h),resample=Image.Resampling.NEAREST)
            
        
        
        self.filetype =image_link[image_link.index("."):]
        self.filename = image_link
        self.sleepTime=1
        self.maxResolution = maxSize
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
    
    def sortRow(self,row):
        
        rowSorted=False
        grid1 = (self.grid[row])
        grid2 = (self.grid[row+1])
        for col in range(self.columns):
                    
            pixela=np.copy(grid1[col])
            pixelb=np.copy(grid2[col])
            
            for val in range(pixela.size):
                
                if pixela[val]!=pixelb[val]:
                    if pixela[val]>pixelb[val]:

                        pixela,pixelb = np.copy(pixelb),np.copy(pixela)

                        # print(pixela,pixelb,2)
                        
                        grid1[col]=pixela
                        
                        grid2[col]=pixelb
                        
                        rowSorted=True
                        # print(grid1[col]is grid2[col],3)
                        

                    break
        return rowSorted
    
    def sortOnce(self):
        tstart = time()
        
        isSorted=True
        for i in range(2):
            for row in range(i,self.rows-1,2):
                if(self.sortRow(row)):
                    isSorted=False

        self.newImage()
        # self.save(f"sortedImages/output{self.filetype}")

        print(f"finished in {time()-tstart}")
        return isSorted


    def sortImage(self):
        while (True):
            if self.sortOnce():
                break
            sleep(self.sleepTime)