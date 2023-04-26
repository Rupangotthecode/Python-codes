import threading
import os

def cube(num):
    print(threading.current_thread().name, os.getpid())
    print('cube=',num*num*num) 

def square(num):
    print(threading.current_thread().name, os.getpid())
    print('square',num*num)

if __name__ == '__main__':
    t1=threading.Thread(target=cube, args=(3,))
    t2=threading.Thread(target=square, args=(3,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()