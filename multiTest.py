from multiprocessing import Pool
import random
import time

x = [[(i,h) for i in range(10)] for h in range(10)]


def get(row):
    print("e",row)






if __name__ == '__main__':
    for e in range(1):
        with Pool(None) as p:
            p.map(get,[i for i in range(20)])
        time.sleep(2)
    print("done")
