from multiprocessing.pool import ThreadPool
from threading import Thread
import subprocess
import time
import random
import sys


def waste_time(counter):
    this_start = time.time()
    print("counter {} start".format(str(counter)))
    i = 100000
    r = i**i
    time.sleep(1.5)
    r = i**i
    this_stop = time.time()
    print("counter {} stop, elapsed: {}".format(str(counter),str(this_stop-this_start)))

def main():
    counter = int(sys.argv[1])
    s = time.time()
    if sys.argv[2] == 'none':
        for i in range(counter):
            counter += 1
            waste_time(counter)
    if sys.argv[2] == 'tp':
        max_t_count = int(sys.argv[3])
        tp = ThreadPool(max_t_count)
        for i in range(counter):
            counter += 1
            tp.apply_async(waste_time,(counter,))
        tp.close()
        tp.join()        

    e = time.time()
    print("type: {}, elapsed: {}".format(str(sys.argv[1]),str(e-s)))

if __name__=="__main__":
    main()
