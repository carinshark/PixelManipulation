from pixelgrid import Pixelgrid
import numpy as np




creechur = Pixelgrid("images1/ship.png")

grid = creechur.grid
# creechur.show()


#clear sorted images





sorted=False
iterations=0

while (not sorted):
    iterations+=1
    sorted=True
    for i in range(2):
        for row in range(i,creechur.rows-i,2):
            
            for col in range(creechur.columns):
                pixela=np.copy(grid[row,col])
                pixelb=np.copy(grid[row+1,col])
                
                for val in range(pixela.size-1,-1,-1):
                    
                    if pixela[val]!=pixelb[val]:
                        if pixela[val]>pixelb[val]:

                            pixela,pixelb = pixelb,pixela

                            # print(pixela,pixelb,2)
                            
                            grid[row,col]=pixela
                            
                            grid[row+1,col]=pixelb
        
                            # print(grid[row,col],grid[row+1,col],3)
                            sorted=False

                        break

    



        creechur.image.copy().save(f"sortedImages/{iterations*2+i}.png")

creechur.show()
