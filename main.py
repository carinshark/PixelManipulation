from pixelgrid import Pixelgrid
from multiprocessing import Process as Thread
import concurrent.futures
from time import time

creechur = Pixelgrid("images1/blues.jpg")



def sortOnce():
    tstart = time()
    for i in range(2):
        allThreads=[]
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(creechur.sortRow,[row for row in range(i,creechur.rows-1,2)])

            for f in results:
                r=f
                creechur.grid[r[0]]=r[1]
                creechur.grid[r[0]+1]=r[2]

        
    
    creechur.save(f"sortedImages/output{creechur.filetype}")
    print(f"finishedd new in {time()-tstart}")
    # self.pic.image=f"sortedImages/output{self.filetype}"

def sortOnceOld():
    tstart = time()
    for i in range(2):
        for row in range(i,creechur.rows-1,2):
            creechur.sortRow(row)

    creechur.save(f"sortedImages/output{creechur.filetype}")

    print(f"finished in {time()-tstart}")

if (__name__=="__main__"):
    sortOnce()
    sortOnceOld()
