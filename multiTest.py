from multiprocessing import Process as Thread
import random
import time

x = [[(i,h) for i in range(10)] for h in range(10)]


def get(row):
    time.sleep()
    print(row)
    return 1


if __name__=="__main__":
    a=[]


    for i in range(10):
        a.append(Thread(target=get,args=(i,)))


    for i in range(10):
        a[i].start()

    for i in range(10):
        (a[i].join())

    print("done")