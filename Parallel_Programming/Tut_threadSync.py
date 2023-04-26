import threading

x=10
# Here the global variable acts as our critical section

def increment(lock):
    global x
    lock.acquire()
    for i in range(5):
        x=x+i
    lock.release()

def decrement(lock):
    global x
    lock.acquire()
    for i in range(5):
        x=x-i
    lock.release()

def perform_tasks():
    lock = threading.Lock()
    t1=threading.Thread(target=increment, args=(lock,))
    t2=threading.Thread(target=decrement, args=(lock,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(f"The final value is {x}")

if __name__ == '__main__':
    for i in range(10):
        perform_tasks()
