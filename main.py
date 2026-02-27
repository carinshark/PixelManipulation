from pixelgrid import Pixelgrid
from multiprocessing import Pool

creechur = Pixelgrid("images1/ship.png")



def sortOnce():
    for i in range(1):
        for i in range(2):
            with Pool(2) as p:
                out = p.map(creechur.sortRow,[row for row in range(i,creechur.rows-1,2)])
                if (True in out):
                    pass
            
        
        creechur.save(f"sortedImages/output{creechur.filetype}")
        # self.pic.image=f"sortedImages/output{self.filetype}"


if (__name__=="__main__"):
     sortOnce()
     sortOnce()