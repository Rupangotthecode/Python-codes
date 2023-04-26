import threading
import time
import random

def producer(items):
    i=1
    while(True):
        time.sleep(random.uniform(0,2))
        items.append(i)
        print(f'Produced:{i}')
        i=i+1

def consumer(items):
    i=1
    while(True):
        time.sleep(random.uniform(0,2))
        if(len(items)==0):
            print('waiting for items')
            continue
        item = items.pop(0)
        print(f'Consumed:{item}')

if __name__=='__main__':
    items=[]

    t1=threading.Thread(target=producer,args=(items,))
    t2=threading.Thread(target=consumer,args=(items,))

    t1.start()
    t2.start()
