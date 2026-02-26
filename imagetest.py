from pixelgrid import Pixelgrid
from guizero import App,Text,Picture,PushButton, select_file,question
import numpy as np


imageName = select_file("which image would you like to sort? RECOMMENDED TO USE SMALLER RESOLUTION PICS",filetypes=
                                 [["images",[".png",".jpg",".jpeg"]]]
                                 )

creechur = Pixelgrid(imageName)

grid = creechur.grid
# creechur.show()

size = creechur.image.size






def sortImage():

    startButton.enabled=False
    startButton.visible=False

    imageSorted=True
    for i in range(2):
        
        for row in range(i,creechur.rows-1,2):
            
            
            for col in range(creechur.columns):
                
                pixela=np.copy(grid[row,col])
                pixelb=np.copy(grid[row+1,col])
                
                for val in range(pixela.size):
                    
                    if pixela[val]!=pixelb[val]:
                        if pixela[val]>pixelb[val]:

                            pixela,pixelb = pixelb,pixela

                            # print(pixela,pixelb,2)
                            
                            grid[row,col]=pixela
                            
                            grid[row+1,col]=pixelb
        
                            # print(grid[row,col],grid[row+1,col],3)
                            imageSorted=False

                        break


        creechur.save(f"sortedImages/output{creechur.filetype}")
        pic.image=f"sortedImages/output{creechur.filetype}"

    if imageSorted:
        print("done")
        pic.cancel(sortImage)

def startSort():
    
    pic.repeat(250,sortImage)
    
    

myApp = App(title="the app")

title = Text(myApp,"sort image!",color="gray",size=24)

pic = Picture(myApp,image=imageName,width=300,height=300)

startButton = PushButton(myApp,command=startSort,text="Click to Start!")



myApp.display()