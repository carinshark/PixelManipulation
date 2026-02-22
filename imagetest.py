from pixelgrid import Pixelgrid
import numpy as np




creechur = Pixelgrid("images1/electricCat.jpeg")

grid = creechur.grid
# creechur.show()


#clear sorted images





is_sorted=False
iterations=0

while (not is_sorted):
    is_sorted=True
    for i in range(2):
        iterations+=1
        print(iterations)
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
                            is_sorted=False

                        break

    



        creechur.save(f"sortedImages/{iterations}.png")
    
    

creechur.show()
